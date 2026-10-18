const PHONE_WA = "905374638838";

const ICONS = {
  dpf: '<rect x="3" y="7" width="18" height="10" rx="3"/><path d="M8 7v10M12 7v10M16 7v10"/>',
  kat: '<rect x="5" y="6" width="14" height="12" rx="4"/><path d="M2 12h3M19 12h3M9 10h6M9 14h6"/>',
  degisim: '<path d="M3 12h11"/><rect x="13" y="8" width="8" height="8" rx="3"/><path d="M6 8 3 12l3 4"/>',
  tamir: '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4 2.6-2.6Z"/>',
  kaynak: '<path d="m4 20 8-8"/><path d="m12 12 3-3 2 2-3 3z"/><path d="M18 3v2M21 6h-2M20 4l-1.2 1.2"/>',
  cihaz: '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/><path d="m7 11 2-2 2 3 2-4 2 3h2"/>',
};
const SERVICES = [
  ["dpf", "DPF temizliği ve değişimi", "Tıkanan partikül filtresini söküp temizliyor, gerekirse değiştiriyoruz."],
  ["kat", "Katalizatör", "Muayeneden kalan, koku yapan veya güç düşüren katalizatörlerin temizliği ve değişimi."],
  ["degisim", "Egzoz değişimi", "Susturucu, ara boru ve arka egzoz değişimi. Orijinal Matay egzoz."],
  ["tamir", "Egzoz tamiri", "Delinen, çatlayan egzozların ve kopan askıların tamiri."],
  ["kaynak", "Kaynak", "Egzoz borusu, manifold ve bağlantı noktalarında kaynak işleri."],
  ["cihaz", "Arıza kontrolü", "Cihazla arıza kodu okuma, sensör ve egzoz hattı kontrolü."],
];

const SYMPTOMS = [
  ["ses", "Egzoz sesi arttı"], ["tikirti", "Alttan tıkırtı sesi"], ["sarkma", "Egzoz sarktı / sürtüyor"],
  ["pas", "Pas veya delik var"], ["koku", "İçeri egzoz kokusu geliyor"], ["curuk", "Çürük yumurta kokusu"],
  ["guc", "Güç kaybı"], ["lamba", "Arıza lambası yandı"], ["dpf", "DPF uyarısı"],
  ["siyah", "Siyah duman"], ["beyaz", "Sürekli beyaz duman"], ["mavi", "Mavimsi duman"],
  ["yakit", "Yakıt tüketimi arttı"], ["muayene", "Muayeneden kaldı"],
];

// Her olası sebep: hangi belirti ne kadar puan verir, aciliyet, yapılacak iş
const CAUSES = [
  { name: "Susturucu delinmiş", w: { ses: 3, pas: 3, koku: 1, muayene: 1 },
    urg: "mid", svc: "Egzoz tamiri veya değişimi", why: "Susturucu içten paslanıp delindiğinde ses belirgin şekilde artar." },
  { name: "Bağlantıdan gaz kaçağı", w: { ses: 2, koku: 3, tikirti: 1, pas: 1 },
    urg: "high", svc: "Kaynak veya egzoz tamiri", why: "Kaçan gaz araç içine girebilir. Karbonmonoksit tehlikesi nedeniyle bekletmeyin." },
  { name: "Egzoz askısı kopmuş", w: { sarkma: 4, tikirti: 3, ses: 1 },
    urg: "high", svc: "Egzoz tamiri", why: "Sarkan egzoz yolda kopup düşebilir. Bu şekilde uzun yol yapmayın." },
  { name: "Manifold çatlağı", w: { tikirti: 2, ses: 2, koku: 2 },
    urg: "mid", svc: "Kaynak", why: "Motor soğukken tıkırtı yapıp ısınınca azalıyorsa manifold çatlağı olabilir." },
  { name: "DPF tıkanmış", w: { dpf: 4, guc: 3, lamba: 2, siyah: 2, yakit: 2 }, diesel: true,
    urg: "high", svc: "DPF temizliği", why: "Tıkalı DPF ile sürmeye devam etmek turboya ve motora zarar verebilir." },
  { name: "Katalizatör arızası", w: { curuk: 4, guc: 2, lamba: 2, muayene: 3, tikirti: 1, yakit: 1 },
    urg: "mid", svc: "Katalizatör temizliği veya değişimi", why: "Katalizatörün içi tıkandığında veya dağıldığında koku, çıngırak sesi ve güç kaybı olur." },
  { name: "Egzoz sensörü arızası", w: { lamba: 3, yakit: 2, dpf: 1, muayene: 1 },
    urg: "low", svc: "Arıza kontrolü (cihazla)", why: "Arıza lambası çoğu zaman bir sensörden gelir. Cihazla kodu okuyunca netleşir." },
  { name: "Motor kaynaklı olabilir", w: { mavi: 4, beyaz: 3, siyah: 1 },
    urg: "mid", svc: "Arıza kontrolü", why: "Mavi duman yağ yakmaya, sürekli beyaz duman motora su karışmasına işaret edebilir. Önce kontrol edip doğru yere yönlendiririz." },
];
const URG = { high: "Acil · Hemen getirin", mid: "Orta · Birkaç gün içinde", low: "Düşük · Uygun bir zamanda" };

const $ = (id) => document.getElementById(id);
const icon = (p, sw = 1.8) => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${p}</svg>`;
const waLink = (text) => `https://wa.me/${PHONE_WA}?text=${encodeURIComponent(text)}`;

$("services").innerHTML = SERVICES.map(([k, t, d]) => `
  <article class="svc">
    <div class="svc-ico">${icon(ICONS[k])}</div>
    <h3>${t}</h3>
    <p>${d}</p>
    <a href="${waLink("Merhaba, " + t.toLowerCase() + " hakkında bilgi almak istiyorum.")}" target="_blank" rel="noopener">Bilgi al ${icon('<path d="M5 12h14M13 6l6 6-6 6"/>', 2.2)}</a>
  </article>`).join("");
$("footSvc").innerHTML = SERVICES.map(([, t]) => `<li><a href="#hizmetler">${t}</a></li>`).join("");
$("symptoms").innerHTML = SYMPTOMS.map(([id, t]) => `<label class="opt"><input type="checkbox" id="s_${id}" value="${id}"><span>${t}</span></label>`).join("");
document.querySelectorAll("[data-wa]").forEach((a) => (a.href = waLink("Merhaba, egzoz için bilgi almak istiyorum.")));
$("yr").textContent = new Date().getFullYear();

// Mobil menü
const nav = $("nav"), menuBtn = $("menuBtn");
menuBtn.addEventListener("click", () => {
  const closed = nav.toggleAttribute("data-closed");
  menuBtn.setAttribute("aria-expanded", String(!closed));
});
nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => { nav.setAttribute("data-closed", ""); menuBtn.setAttribute("aria-expanded", "false"); }));

// Çalışma saatleri ve açık/kapalı (Türkiye saati)
const DAYS = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"];
function trNow() {
  try {
    const p = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Istanbul", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(new Date());
    const g = (t) => p.find((x) => x.type === t).value;
    return { day: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"].indexOf(g("weekday")), mins: parseInt(g("hour"), 10) % 24 * 60 + parseInt(g("minute"), 10) };
  } catch (e) { const d = new Date(); return { day: (d.getDay() + 6) % 7, mins: d.getHours() * 60 + d.getMinutes() }; }
}
const now = trNow();
$("hours").innerHTML = DAYS.map((d, i) => {
  const c = i === now.day ? ' class="today"' : "";
  return `<span${c}>${d}${i === now.day ? " · Bugün" : ""}</span><span${c}>${i === 6 ? '<span class="off">Kapalı</span>' : "09:00 – 19:00"}</span>`;
}).join("");
const isOpen = now.day !== 6 && now.mins >= 540 && now.mins < 1140;
$("status").classList.add(isOpen ? "open" : "closed");
$("statusText").textContent = isOpen ? "Şu an açık" : "Şu an kapalı";

// Teşhis: en yüksek puanlı tek sebep
function diagnose(sel, fuel) {
  let best = null;
  CAUSES.forEach((c) => {
    let s = 0;
    sel.forEach((k) => { s += c.w[k] || 0; });
    if (c.diesel && (fuel === "benzin" || fuel === "lpg")) s *= 0.3;
    if (c.diesel && fuel === "dizel") s *= 1.2;
    if (s >= 2 && (!best || s > best.score)) best = { ...c, score: s };
  });
  return best;
}

let lastMsg = "";
$("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const sel = [...document.querySelectorAll("#symptoms input:checked")].map((i) => i.value);
  $("err").hidden = sel.length > 0;
  if (!sel.length) { $("result").hidden = true; return; }

  const fuel = $("fuel").value;
  const d = diagnose(sel, fuel);
  if (d) {
    $("dName").textContent = d.name;
    $("dUrg").className = "urg " + d.urg;
    $("dUrg").textContent = URG[d.urg];
    $("dUrg").hidden = false;
    $("dWhy").textContent = d.why;
    $("dSvc").innerHTML = icon(ICONS.tamir, 2) + "Yapılacak iş: " + d.svc;
  } else {
    $("dName").textContent = "Net bir sonuç çıkmadı";
    $("dUrg").hidden = true;
    $("dWhy").textContent = "Bize yazın veya aracı getirin, cihazla kontrol edelim.";
    $("dSvc").textContent = "";
  }

  const symText = SYMPTOMS.filter(([id]) => sel.includes(id)).map(([, t]) => "- " + t).join("\n");
  const car = [$("brand").value.trim(), $("year").value.trim(), fuel && $("fuel").selectedOptions[0].text, $("km").value.trim() && $("km").value.trim() + " km"].filter(Boolean).join(", ");
  const note = $("note").value.trim();
  lastMsg = "Merhaba, siteden yazıyorum.\n"
    + (car ? "Araç: " + car + "\n" : "")
    + "Belirtiler:\n" + symText + "\n"
    + (note ? "Not: " + note + "\n" : "")
    + (d ? "Sitedeki ön tahmin: " + d.name + "\n" : "")
    + "Ne zaman getirebilirim?";
  $("msg").textContent = lastMsg;
  $("waSend").href = waLink(lastMsg);
  $("result").hidden = false;
  $("result").scrollIntoView({ block: "nearest" });
});

$("copy").addEventListener("click", () => {
  const done = () => { $("copy").textContent = "Kopyalandı"; setTimeout(() => ($("copy").textContent = "Mesajı Kopyala"), 2000); };
  const fallback = () => { const r = document.createRange(); r.selectNodeContents($("msg")); const s = getSelection(); s.removeAllRanges(); s.addRange(r); $("copy").textContent = "Seçildi, kopyalayabilirsiniz"; };
  try { navigator.clipboard.writeText(lastMsg).then(done, fallback); } catch (e) { fallback(); }
});
