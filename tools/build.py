"""Siteyi şablonlardan üretir.

Kullanım:
    python tools/build.py

Üretilen dosyalar: index.html, hizmetler/<slug>/index.html, 404.html, sitemap.xml, robots.txt
Ek bağımlılık gerektirmez (sadece Python 3.8+).
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from site_data import BASE_URL, BUSINESS, HOME_FAQ, ICONS, SERVICES  # noqa: E402

TEMPLATES = ROOT / "templates"
TODAY = dt.date.today().isoformat()


def read(name: str) -> str:
    return (TEMPLATES / name).read_text(encoding="utf-8")


def render(tpl: str, **values: str) -> str:
    for key, value in values.items():
        tpl = tpl.replace("{{" + key + "}}", value)
    if "{{" in tpl:
        start = tpl.index("{{")
        raise ValueError(f"Doldurulmamış alan: {tpl[start:start + 40]}")
    return tpl


def _os_path(path: Path) -> Path:
    # Windows'ta 260 karakteri aşan klasör yolları için uzun yol öneki
    if os.name == "nt" and not str(path).startswith("\\\\?\\"):
        return Path("\\\\?\\" + str(path.resolve()))
    return path


def write(path: Path, text: str) -> None:
    target = _os_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")
    print("  yazıldı:", path.relative_to(ROOT).as_posix())


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def icon(key: str, stroke: float = 1.8) -> str:
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>')


ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')


def wa_link(text: str) -> str:
    return f"https://wa.me/{BUSINESS['whatsapp']}?text={quote(text)}"


def service_url(s: dict) -> str:
    return f"hizmetler/{s['slug']}/"


def faq_html(items) -> str:
    return "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in items)


def jsonld(*objects: dict) -> str:
    return "\n".join(
        '<script type="application/ld+json">\n' + json.dumps(o, ensure_ascii=False, indent=2) + "\n</script>"
        for o in objects
    )


def business_ld() -> dict:
    b = BUSINESS
    return {
        "@context": "https://schema.org",
        "@type": "AutoRepair",
        "@id": BASE_URL + "/#isletme",
        "name": b["name"],
        "description": "Esenyurt Fatih Oto Sanayi Sitesi'nde egzoz, katalizatör ve DPF servisi. Matay yetkili servisi.",
        "url": BASE_URL + "/",
        "image": BASE_URL + "/assets/img/og-image.png",
        "logo": BASE_URL + "/assets/img/apple-touch-icon.png",
        "telephone": b["gsm_intl"],
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": b["gsm_intl"], "contactType": "customer service", "availableLanguage": "Turkish"},
            {"@type": "ContactPoint", "telephone": b["landline_intl"], "contactType": "customer service", "availableLanguage": "Turkish"},
        ],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": b["street"],
            "addressLocality": b["district"],
            "addressRegion": b["city"],
            "addressCountry": "TR",
        },
        "hasMap": b["maps"],
        "areaServed": [{"@type": "Place", "name": n} for n in b["area_served"]],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "19:00",
        }],
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{BASE_URL}/{service_url(s)}"}}
            for s in SERVICES
        ],
    }


def faq_ld(items) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items
        ],
    }


def page(*, root: str, title: str, description: str, canonical: str, content: str, ld: str, robots: str = "index, follow") -> str:
    nav_services = "".join(f'<li><a href="{root}{service_url(s)}">{esc(s["name"])}</a></li>' for s in SERVICES)
    foot_services = nav_services
    header = render(read("partials/header.html"), root=root, nav_services=nav_services)
    footer = render(read("partials/footer.html"), root=root, foot_services=foot_services,
                    maps=esc(BUSINESS["maps"]), year=str(dt.date.today().year))
    return render(read("base.html"), title=esc(title), description=esc(description), canonical=canonical,
                  robots=robots, root=root, base=BASE_URL, jsonld=ld, header=header, content=content, footer=footer)


def build_home() -> None:
    cards = "".join(f'''
      <article class="svc">
        <div class="svc-ico">{icon(s["icon"])}</div>
        <h3><a href="{service_url(s)}">{esc(s["name"])}</a></h3>
        <p>{esc(s["short"])}</p>
        <a class="more" href="{service_url(s)}">Detaylı bilgi {ARROW}</a>
      </article>''' for s in SERVICES)
    content = render(read("home.html"), service_cards=cards + "\n    ", faq=faq_html(HOME_FAQ))
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": BUSINESS["name"], "url": BASE_URL + "/", "inLanguage": "tr-TR"}
    write(ROOT / "index.html", page(
        root="",
        title="Esenyurt Egzoz Servisi | DPF Temizliği, Katalizatör | Gümüşhaneliler Egzoz",
        description="Esenyurt Fatih Oto Sanayi Sitesi'nde Matay yetkili egzoz servisi. DPF temizliği, katalizatör, egzoz değişimi, egzoz tamiri ve kaynak. Online arıza bulucu ile sorununuzu öğrenin.",
        canonical=BASE_URL + "/",
        content=content,
        ld=jsonld(business_ld(), website, faq_ld(HOME_FAQ)),
    ))


def build_services() -> None:
    b = BUSINESS
    for s in SERVICES:
        root = "../../"
        others = "".join(
            f'<li><a href="{root}{service_url(o)}">{icon(o["icon"])}<span>{esc(o["name"])}</span></a></li>'
            for o in SERVICES if o is not s
        )
        content = render(
            read("service.html"),
            root=root,
            name=esc(s["name"]),
            h1=esc(s["title"]),
            lead=esc(s["lead"]),
            icon=icon(s["icon"]),
            body="\n      ".join(f"<p>{esc(p)}</p>" for p in s["body"]),
            symptoms="".join(f"<li>{esc(x)}</li>" for x in s["symptoms"]),
            process="".join(f"<li><b>{esc(t)}</b><span>{esc(d)}</span></li>" for t, d in s["process"]),
            faq=faq_html(s["faq"]),
            other_services=others,
            wa_link=esc(wa_link(f"Merhaba, {s['name'].lower()} hakkında bilgi almak istiyorum.")),
            gsm=b["gsm"], gsm_intl=b["gsm_intl"], landline=b["landline"], landline_intl=b["landline_intl"],
            contact_person=esc(b["contact_person"]), maps=esc(b["maps"]),
        )
        url = f"{BASE_URL}/{service_url(s)}"
        service_ld = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": s["title"],
            "serviceType": s["name"],
            "description": s["description"],
            "url": url,
            "provider": {"@id": BASE_URL + "/#isletme"},
            "areaServed": [{"@type": "Place", "name": n} for n in b["area_served"]],
        }
        crumbs_ld = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": BASE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": "Hizmetler", "item": BASE_URL + "/#hizmetler"},
                {"@type": "ListItem", "position": 3, "name": s["name"], "item": url},
            ],
        }
        write(ROOT / "hizmetler" / s["slug"] / "index.html", page(
            root=root,
            title=f"{s['title']} | Gümüşhaneliler Egzoz",
            description=s["description"],
            canonical=url,
            content=content,
            ld=jsonld(business_ld(), service_ld, crumbs_ld, faq_ld(s["faq"])),
        ))


def build_404() -> None:
    root = BASE_URL + "/"
    content = f'''<section class="notfound">
  <div class="in">
    <span class="eyebrow">Hata 404</span>
    <h1>Aradığınız sayfa bulunamadı</h1>
    <p>Sayfa taşınmış ya da silinmiş olabilir. Ana sayfadan devam edebilir veya bizi arayabilirsiniz.</p>
    <div class="ctas"><a class="btn red" href="{root}">Ana Sayfaya Dön</a><a class="btn outline" href="tel:{BUSINESS["gsm_intl"]}">{BUSINESS["gsm"]}</a></div>
  </div>
</section>'''
    write(ROOT / "404.html", page(root=root, title="Sayfa bulunamadı | Gümüşhaneliler Egzoz",
                                  description="Aradığınız sayfa bulunamadı.", canonical=root, content=content,
                                  ld="", robots="noindex"))


def build_sitemap() -> None:
    urls = [(BASE_URL + "/", "1.0")] + [(f"{BASE_URL}/{service_url(s)}", "0.8") for s in SERVICES]
    body = "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    write(ROOT / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")
    write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")


if __name__ == "__main__":
    print("Site üretiliyor...")
    build_home()
    build_services()
    build_404()
    build_sitemap()
    print("Bitti.")
