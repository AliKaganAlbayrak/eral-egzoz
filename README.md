<div align="center">

<img src="assets/img/favicon.svg" width="72" alt="Gümüşhaneliler Egzoz logo">

# Gümüşhaneliler Egzoz

**Website for an exhaust, catalytic converter and DPF repair shop in Esenyurt, Istanbul**

[Live site](https://alikaganalbayrak.github.io/gumushaneliler-egzoz/) · [Changelog](CHANGELOG.md)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-build-3776AB?logo=python&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?logo=githubpages&logoColor=white)

</div>

---

## About

Gümüşhaneliler Egzoz is an exhaust repair shop in Fatih Oto Sanayi Sitesi, Esenyurt (Istanbul) and an authorized Matay exhaust service. This website lets customers **describe their car's symptoms online, see the most likely fault and how urgent it is**, and then **contact the shop on WhatsApp with one tap**. The message arrives pre-filled with the car details and symptoms, so the mechanic knows the problem before picking up the phone.

The site needs no server, database or framework. Pages are rendered from templates by a small Python script and served as plain HTML, CSS and JavaScript on GitHub Pages at no cost.

> The site content is in Turkish because it is written for the shop's local customers. Code, comments and documentation are in English.

## Features

| Feature | Description |
| --- | --- |
| **Fault finder** | Customers pick from 14 symptoms and enter their car. A weighted scoring model shows the single most likely fault with an urgency level (high / medium / low) and links to the matching service page. |
| **Pre-filled WhatsApp message** | Symptoms, car details and the estimate are combined into one message sent through a `wa.me` deep link. |
| **Live open / closed status** | Computed in the browser from Europe/Istanbul time. |
| **Service pages** | One page per service with symptoms, a step-by-step process and an FAQ. |
| **Local SEO** | Per-page titles, descriptions and canonical URLs, `sitemap.xml`, Open Graph share image and schema.org structured data (`AutoRepair`, `Service`, `FAQPage`, `BreadcrumbList`). |
| **Responsive** | Mobile navigation and a sticky WhatsApp / call dock on small screens. |
| **Accessible** | Semantic landmarks, visible focus states, labelled form controls and reduced-motion support. |

## Project structure

```
gumushaneliler-egzoz/
├── templates/               # Page templates (edit these)
│   ├── base.html            # <head>, SEO tags, page shell
│   ├── home.html            # Home page content
│   ├── service.html         # Service page template
│   └── partials/            # Header and footer
├── tools/
│   ├── site_data.py         # Business details, service copy, FAQ
│   ├── build.py             # Renders the site from the templates
│   └── make_images.py       # Generates the share image and touch icon
├── assets/
│   ├── css/style.css        # Styles (design tokens in :root)
│   ├── js/main.js           # Fault finder, navigation, opening hours
│   └── img/                 # Logo, icons, share image
├── index.html               # generated
├── hizmetler/<service>/     # generated, one page per service
├── 404.html                 # generated
├── sitemap.xml, robots.txt  # generated
├── CHANGELOG.md
└── README.md
```

> Generated files (`index.html`, `hizmetler/`, `404.html`, `sitemap.xml`, `robots.txt`) are committed so GitHub Pages can serve them, but they should not be edited by hand. Change `templates/` or `tools/site_data.py` and rebuild.

## Development

Requirements: Python 3.8 or newer. No other dependencies.

```bash
python tools/build.py
```

Preview locally:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

Regenerate the share image and touch icon (optional):

```bash
pip install pillow
python tools/make_images.py
```

## Editing content

| What | Where |
| --- | --- |
| Phone numbers, address, hours, service area | `BUSINESS` in `tools/site_data.py`, plus `templates/` |
| WhatsApp number used by the fault finder | `PHONE_WA` in `assets/js/main.js` |
| Services and service page copy | `SERVICES` in `tools/site_data.py` |
| Home page FAQ | `HOME_FAQ` in `tools/site_data.py` |
| Symptoms and possible faults | `SYMPTOMS` and `CAUSES` in `assets/js/main.js` |
| Colors and fonts | `:root` at the top of `assets/css/style.css` |
| Site URL (custom domain) | `BASE_URL` in `tools/site_data.py` |

To add a service page, append an entry to `SERVICES` and run `python tools/build.py`. The navigation, footer, sitemap and "other services" sidebar update automatically.

### How the fault finder works

Every fault in `CAUSES` has a weight per symptom (`w`). The weights of the selected symptoms are summed and the highest-scoring fault is shown. DPF faults are boosted for diesel cars and damped for petrol and LPG cars. Faults scoring below 2 are ignored; if nothing qualifies, the customer is asked to get in touch for an inspection.

```js
{ name: "Fault name", w: { ses: 3, koku: 2 }, urg: "mid", svc: "Recommended job", page: "egzoz-tamiri", why: "Short explanation." }
```

`urg` is one of `high`, `mid` or `low`.

> The fault finder only gives a preliminary estimate. A definitive diagnosis is made at the shop.

## SEO

The site targets local searches such as "Esenyurt egzoz" and "Esenyurt DPF temizliği":

- Every page has its own title, meta description and canonical URL.
- Each service has a dedicated page that can rank on its own.
- `sitemap.xml` lists every page and `robots.txt` points to it.
- schema.org structured data describes the business, its services, opening hours and FAQs.

Recommended steps for the site owner:

1. Create a **Google Business Profile** at [business.google.com](https://business.google.com) and link this website. This is the most effective way to appear in Maps and "near me" searches.
2. Add the site to **Google Search Console** at [search.google.com/search-console](https://search.google.com/search-console) and submit `sitemap.xml`.
3. Ask customers for Google reviews.

## Deployment

The site is deployed with **GitHub Pages** from the `main` branch. Every push to `main` goes live within a few minutes.

To use a custom domain (for example `gumushanelileregzoz.com`):

1. Register the domain and point its DNS records to GitHub Pages.
2. Add a `CNAME` file containing the domain to the repository root.
3. Set `BASE_URL` in `tools/site_data.py` to the new address and run `python tools/build.py`.

## Roadmap

- [x] Fault finder with pre-filled WhatsApp message
- [x] Corporate design based on the shop's business card
- [x] SEO metadata and structured data
- [x] Dedicated service pages, sitemap and share image
- [ ] Real photos of the shop and completed work
- [ ] Google Business Profile and map location
- [ ] Google Search Console
- [ ] Custom domain
- [ ] Customer reviews
- [ ] Free-text fault description with AI assistance

## Contact

**Gümüşhaneliler Egzoz**
Fatih Oto Sanayi Sitesi C6 Blok No:6, Esenyurt / Istanbul, Türkiye
Erdal Albayrak: +90 537 463 88 38 · Shop: +90 212 690 32 18
Monday–Saturday, 09:00–19:00

## License

© Gümüşhaneliler Egzoz. All rights reserved. The source code is public for reference; the business name, logo and content may not be reused without permission.
