<div align="center">

<img src="assets/img/favicon.svg" width="72" alt="Gümüşhaneliler 2 Egzoz logosu">

# Gümüşhaneliler 2 Egzoz

**Esenyurt Fatih Oto Sanayi Sitesi'nde egzoz, katalizatör ve DPF servisi için web sitesi**

[Canlı site](https://alikaganalbayrak.github.io/gumushaneliler-egzoz/) · [Değişiklikler](CHANGELOG.md)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?logo=githubpages&logoColor=white)

</div>

---

## Proje hakkında

Bu site, müşterilerin egzozla ilgili yaşadıkları sorunu internetten anlatıp **olası arızayı ve aciliyetini öğrenmesi**, ardından **tek tuşla WhatsApp'tan dükkâna ulaşması** için hazırlandı.

Site herhangi bir sunucu, veritabanı ya da kütüphane gerektirmez. Sadece HTML, CSS ve JavaScript ile yazılmıştır, bu yüzden ücretsiz olarak GitHub Pages'te yayınlanabilir.

## Özellikler

| Özellik | Açıklama |
| --- | --- |
| **Arıza bulucu** | Müşteri 14 belirtiden seçer, aracını yazar. Site en olası sorunu ve aciliyet derecesini (Acil / Orta / Düşük) gösterir. |
| **Hazır WhatsApp mesajı** | Seçilen belirtiler, araç bilgisi ve ön tahmin tek mesajda toplanır. Usta telefonu açmadan sorunu görür. |
| **Açık / kapalı durumu** | Türkiye saatine göre dükkânın şu an açık olup olmadığını gösterir. |
| **Hizmet kartları** | Her hizmetten, o hizmetin adıyla hazır WhatsApp mesajı açılır. |
| **SSS** | DPF, katalizatör, muayene, fiyat ve randevu ile ilgili sık sorulan sorular. |
| **Mobil uyumlu** | Telefonda menü, ekranın altında sabit WhatsApp ve Ara butonları. |
| **SEO** | Açıklama etiketleri ve Google için `AutoRepair` yapısal verisi (schema.org). |

## Proje yapısı

```
gumushaneliler-egzoz/
├── index.html            # Sayfanın tamamı
├── assets/
│   ├── css/style.css     # Tasarım (renkler en üstte :root içinde)
│   ├── js/main.js        # Arıza bulucu, saatler, WhatsApp bağlantıları
│   └── img/favicon.svg   # Logo / sekme ikonu
├── robots.txt
├── CHANGELOG.md
└── README.md
```

## Bilgisayarda çalıştırma

`index.html` dosyasına çift tıklamak yeterlidir. Yerel bir sunucuyla açmak için:

```bash
python -m http.server 8000
```

Sonra tarayıcıda `http://localhost:8000` adresini açın.

## Bilgileri güncelleme

| Ne değişecek | Nerede |
| --- | --- |
| WhatsApp numarası | `assets/js/main.js` içinde `PHONE_WA` |
| Telefon, adres, saatler (yazılar) | `index.html` |
| Hizmetler | `assets/js/main.js` içinde `SERVICES` |
| Belirtiler ve olası arızalar | `assets/js/main.js` içinde `SYMPTOMS` ve `CAUSES` |
| Renkler ve yazı tipleri | `assets/css/style.css` en üstteki `:root` |

### Arıza bulucu nasıl çalışır

`CAUSES` listesindeki her arızanın, belirtilere göre puanları vardır (`w`). Müşterinin seçtiği belirtilerin puanları toplanır ve en yüksek puanlı arıza gösterilir. Dizel araçlarda DPF puanı artırılır, benzinli araçlarda azaltılır. Yeni bir arıza eklemek için listeye bir satır eklemek yeterlidir:

```js
{ name: "Arıza adı", w: { ses: 3, koku: 2 }, urg: "mid", svc: "Yapılacak iş", why: "Kısa açıklama." }
```

`urg` değeri `high` (acil), `mid` (orta) veya `low` (düşük) olabilir.

> Arıza bulucu yalnızca bir ön tahmindir. Kesin teşhis için araç dükkânda kontrol edilir.

## Yayınlama

Site, `main` dalından **GitHub Pages** ile yayınlanır. `main` dalına gönderilen her değişiklik birkaç dakika içinde canlı siteye yansır.

Kendi alan adını (ör. `gumushaneliler2egzoz.com`) bağlamak için depoya bir `CNAME` dosyası eklenir ve alan adının DNS ayarlarından GitHub Pages'e yönlendirme yapılır.

## Yol haritası

- [x] Arıza bulucu ve WhatsApp'a hazır mesaj
- [x] Kartvizitteki kimliğe uygun kurumsal tasarım
- [x] SEO etiketleri ve yapısal veri
- [ ] Dükkânın ve yapılan işlerin gerçek fotoğrafları
- [ ] Google İşletme Profili ve harita konumu
- [ ] Kendi alan adı
- [ ] Müşteri yorumları
- [ ] Serbest yazıyla arıza tarifi (yapay zekâ desteği)

## İletişim

**Gümüşhaneliler 2 Egzoz**
Fatih Oto Sanayi Sitesi C6 Blok No:6, Esenyurt / İstanbul
Erdal Albayrak: 0537 463 88 38 · Dükkân: 0212 690 32 18
Pazartesi–Cumartesi 09:00–19:00

---

<sub>© Gümüşhaneliler 2 Egzoz. Tüm hakları saklıdır.</sub>
