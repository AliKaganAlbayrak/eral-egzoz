/* ER AL Egzoz — client-side behaviour
 * - Mobile navigation
 * - Open / closed status and opening hours table (Europe/Istanbul time)
 * - WhatsApp deep links
 * - Fault finder (home page only)
 */
(() => {
  "use strict";

  const PHONE_WA = "905374638838";

  const $ = (id) => document.getElementById(id);
  const waLink = (text) => `https://wa.me/${PHONE_WA}?text=${encodeURIComponent(text)}`;

  /* ---------- WhatsApp links ---------- */
  document.querySelectorAll("[data-wa]").forEach((a) => {
    a.href = waLink("Merhaba, egzoz için bilgi almak istiyorum.");
  });

  /* ---------- Mobile navigation ---------- */
  const nav = $("nav");
  const menuBtn = $("menuBtn");
  if (nav && menuBtn) {
    const close = () => { nav.setAttribute("data-closed", ""); menuBtn.setAttribute("aria-expanded", "false"); };
    menuBtn.addEventListener("click", () => {
      const closed = nav.toggleAttribute("data-closed");
      menuBtn.setAttribute("aria-expanded", String(!closed));
    });
    nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", close));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
  }

  /* ---------- Opening hours (Istanbul time) ---------- */
  const OPEN_MIN = 9 * 60;
  const CLOSE_MIN = 19 * 60;
  const DAYS = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"];

  function istanbulNow() {
    try {
      const parts = new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/Istanbul", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false,
      }).formatToParts(new Date());
      const get = (t) => parts.find((p) => p.type === t).value;
      return {
        day: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].indexOf(get("weekday")),
        mins: (parseInt(get("hour"), 10) % 24) * 60 + parseInt(get("minute"), 10),
      };
    } catch (e) {
      const d = new Date();
      return { day: (d.getDay() + 6) % 7, mins: d.getHours() * 60 + d.getMinutes() };
    }
  }

  const now = istanbulNow();
  const isOpen = now.day !== 6 && now.mins >= OPEN_MIN && now.mins < CLOSE_MIN;
  const status = $("status");
  if (status) {
    status.classList.add(isOpen ? "open" : "closed");
    $("statusText").textContent = isOpen ? "Şu an açık" : "Şu an kapalı";
  }
  const hours = $("hours");
  if (hours) {
    hours.innerHTML = DAYS.map((d, i) => {
      const c = i === now.day ? ' class="today"' : "";
      const val = i === 6 ? '<span class="off">Kapalı</span>' : "09:00 – 19:00";
      return `<span${c}>${d}${i === now.day ? " · Bugün" : ""}</span><span${c}>${val}</span>`;
    }).join("");
  }

  /* ---------- Fault finder ---------- */
  const form = $("form");
  const symptomsEl = $("symptoms");
  if (!form || !symptomsEl) return;

  const SYMPTOMS = [
    ["ses", "Egzoz sesi arttı"], ["tikirti", "Alttan tıkırtı sesi"], ["sarkma", "Egzoz sarktı / sürtüyor"],
    ["pas", "Pas veya delik var"], ["koku", "İçeri egzoz kokusu geliyor"], ["curuk", "Çürük yumurta kokusu"],
    ["guc", "Güç kaybı"], ["lamba", "Arıza lambası yandı"], ["dpf", "DPF uyarısı"],
    ["siyah", "Siyah duman"], ["beyaz", "Sürekli beyaz duman"], ["mavi", "Mavimsi duman"],
    ["yakit", "Yakıt tüketimi arttı"], ["muayene", "Muayeneden kaldı"],
  ];

  // Each possible fault: symptom weights (w), urgency (urg), recommended job (svc), service page slug (page)
  const CAUSES = [
    { name: "Susturucu delinmiş", w: { ses: 3, pas: 3, koku: 1, muayene: 1 }, urg: "mid",
      svc: "Egzoz tamiri veya değişimi", page: "egzoz-degisimi",
      why: "Susturucu içten paslanıp delindiğinde ses belirgin şekilde artar." },
    { name: "Bağlantıdan gaz kaçağı", w: { ses: 2, koku: 3, tikirti: 1, pas: 1 }, urg: "high",
      svc: "Kaynak veya egzoz tamiri", page: "egzoz-tamiri",
      why: "Kaçan gaz araç içine girebilir. Karbonmonoksit tehlikesi nedeniyle bekletmeyin." },
    { name: "Egzoz askısı kopmuş", w: { sarkma: 4, tikirti: 3, ses: 1 }, urg: "high",
      svc: "Egzoz tamiri", page: "egzoz-tamiri",
      why: "Sarkan egzoz yolda kopup düşebilir. Bu şekilde uzun yol yapmayın." },
    { name: "Manifold çatlağı", w: { tikirti: 2, ses: 2, koku: 2 }, urg: "mid",
      svc: "Kaynak", page: "egzoz-kaynak",
      why: "Motor soğukken tıkırtı yapıp ısınınca azalıyorsa manifold çatlağı olabilir." },
    { name: "DPF tıkanmış", w: { dpf: 4, guc: 3, lamba: 2, siyah: 2, yakit: 2 }, diesel: true, urg: "high",
      svc: "DPF temizliği", page: "dpf-temizligi",
      why: "Tıkalı DPF ile sürmeye devam etmek turboya ve motora zarar verebilir." },
    { name: "Katalizatör arızası", w: { curuk: 4, guc: 2, lamba: 2, muayene: 3, tikirti: 1, yakit: 1 }, urg: "mid",
      svc: "Katalizatör temizliği veya değişimi", page: "katalizator",
      why: "Katalizatörün içi tıkandığında veya dağıldığında koku, çıngırak sesi ve güç kaybı olur." },
    { name: "Egzoz sensörü arızası", w: { lamba: 3, yakit: 2, dpf: 1, muayene: 1 }, urg: "low",
      svc: "Arıza kontrolü (cihazla)", page: "ariza-kontrolu",
      why: "Arıza lambası çoğu zaman bir sensörden gelir. Cihazla kodu okuyunca netleşir." },
    { name: "Motor kaynaklı olabilir", w: { mavi: 4, beyaz: 3, siyah: 1 }, urg: "mid",
      svc: "Arıza kontrolü", page: "ariza-kontrolu",
      why: "Mavi duman yağ yakmaya, sürekli beyaz duman motora su karışmasına işaret edebilir. Önce kontrol edip doğru yere yönlendiririz." },
  ];
  const URG = { high: "Acil · Hemen getirin", mid: "Orta · Birkaç gün içinde", low: "Düşük · Uygun bir zamanda" };

  symptomsEl.innerHTML = SYMPTOMS.map(([id, t]) =>
    `<label class="opt"><input type="checkbox" id="s_${id}" value="${id}"><span>${t}</span></label>`).join("");

  function diagnose(selected, fuel) {
    let best = null;
    CAUSES.forEach((c) => {
      let score = selected.reduce((sum, k) => sum + (c.w[k] || 0), 0);
      if (c.diesel && (fuel === "benzin" || fuel === "lpg")) score *= 0.3;
      if (c.diesel && fuel === "dizel") score *= 1.2;
      if (score >= 2 && (!best || score > best.score)) best = { ...c, score };
    });
    return best;
  }

  let lastMsg = "";
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const selected = [...symptomsEl.querySelectorAll("input:checked")].map((i) => i.value);
    $("err").hidden = selected.length > 0;
    if (!selected.length) { $("result").hidden = true; return; }

    const fuel = $("fuel").value;
    const d = diagnose(selected, fuel);
    if (d) {
      $("dName").textContent = d.name;
      $("dUrg").className = "urg " + d.urg;
      $("dUrg").textContent = URG[d.urg];
      $("dUrg").hidden = false;
      $("dWhy").textContent = d.why;
      $("dSvc").innerHTML = `Yapılacak iş: <a href="hizmetler/${d.page}/">${d.svc}</a>`;
    } else {
      $("dName").textContent = "Net bir sonuç çıkmadı";
      $("dUrg").hidden = true;
      $("dWhy").textContent = "Bize yazın veya aracı getirin, cihazla kontrol edelim.";
      $("dSvc").textContent = "";
    }

    const symText = SYMPTOMS.filter(([id]) => selected.includes(id)).map(([, t]) => "- " + t).join("\n");
    const km = $("km").value.trim();
    const car = [
      $("brand").value.trim(),
      $("year").value.trim(),
      fuel && $("fuel").selectedOptions[0].text,
      km && km + " km",
    ].filter(Boolean).join(", ");
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
    const btn = $("copy");
    const done = () => { btn.textContent = "Kopyalandı"; setTimeout(() => (btn.textContent = "Mesajı Kopyala"), 2000); };
    const fallback = () => {
      const range = document.createRange();
      range.selectNodeContents($("msg"));
      const sel = getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      btn.textContent = "Seçildi, kopyalayabilirsiniz";
    };
    try { navigator.clipboard.writeText(lastMsg).then(done, fallback); } catch (e) { fallback(); }
  });
})();
