<div align="center">

<img src="assets/img/favicon.svg" width="72" alt="Gümüşhaneliler Egzoz logosu">

# Gümüşhaneliler Egzoz

**Esenyurt Fatih Oto Sanayi Sitesi'nde egzoz, katalizatör ve DPF servisi için web sitesi**

[Canlı site](https://alikaganalbayrak.github.io/gumushaneliler-egzoz/) · [Değişiklikler](CHANGELOG.md)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-derleme-3776AB?logo=python&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?logo=githubpages&logoColor=white)

</div>

---

## Proje hakkında

Bu site, müşterilerin egzozla ilgili yaşadıkları sorunu internetten anlatıp **olası arızayı ve aciliyetini öğrenmesi**, ardından **tek tuşla WhatsApp'tan dükkâna ulaşması** için hazırlandı.

Site herhangi bir sunucu, veritabanı ya da kütüphane gerektirmez. Sayfalar küçük bir Python betiğiyle şablonlardan üretilir ve düz HTML, CSS ve JavaScript olarak ücretsiz GitHub Pages'te yayınlanır.

## Özellikler

| Özellik | Açıklama |
| --- | --- |
| **Arıza bulucu** | Müşteri 14 belirtiden seçer, aracını yazar. Site en olası sorunu ve aciliyet derecesini (Acil / Orta / Düşük) gösterir. |
| **Hazır WhatsApp mesajı** | Seçilen belirtiler, araç bilgisi ve ön tahmin tek mesajda toplanır. Usta telefonu açmadan sorunu görür. |
| **Açık / kapalı durumu** | Türkiye saatine göre dükkânın şu an açık olup olmadığını gösterir. |
| **Hizmet kartları** | Her hizmetten, o hizmetin adıyla hazır WhatsApp mesajı açılır. |
| **SSS** | DPF, katalizatör, muayene, fiyat ve randevu ile ilgili sık sorulan sorular. |
| **Mobil uyumlu** | Telefonda menü, ekranın altında sabit WhatsApp ve Ara butonları. |
| **Hizmet sayfaları** | Her hizmetin kendi sayfası var: belirtiler, çalışma adımları ve SSS. |
| **SEO** | Sayfaya özel başlık ve açıklamalar, `sitemap.xml`, paylaşım görseli ve schema.org yapısal verisi (`AutoRepair`, `Service`, `FAQPage`, `BreadcrumbList`). |

## Proje yapısı

```
gumushaneliler-egzoz/
├── templates/               # Sayfa şablonları (DÜZENLENEN dosyalar)
│   ├── base.html            # <head>, SEO etiketleri, sayfa iskeleti
│   ├── home.html            # Ana sayfa içeriği
│   ├── service.html         # Hizmet sayfası şablonu
│   └── partials/            # Üst menü ve alt bilgi
├── tools/
│   ├── site_data.py         # İşletme bilgileri, hizmet metinleri, SSS
│   ├── build.py             # Şablonlardan siteyi üretir
│   └── make_images.py       # Paylaşım görseli ve telefon ikonu
├── assets/
│   ├── css/style.css        # Tasarım (renkler en üstte :root içinde)
│   ├── js/main.js           # Arıza bulucu, menü, saatler
│   └── img/                 # Logo, ikonlar, paylaşım görseli
├── index.html               # ÜRETİLİR
├── hizmetler/<hizmet>/      # ÜRETİLİR, her hizmete bir sayfa
├── 404.html                 # ÜRETİLİR
├── sitemap.xml, robots.txt  # ÜRETİLİR
├── CHANGELOG.md
└── README.md
```

> `index.html`, `hizmetler/`, `404.html`, `sitemap.xml` ve `robots.txt` elle düzenlenmez. Değişiklik `templates/` veya `tools/site_data.py` içinde yapılır, sonra site yeniden üretilir.

## Geliştirme

Gereken tek şey Python 3.8 veya üstü.

```bash
python tools/build.py
```

Siteyi bilgisayarda görmek için:

```bash
python -m http.server 8000
```

Sonra tarayıcıda `http://localhost:8000` adresini açın.

Paylaşım görselini yeniden üretmek için (isteğe bağlı):

```bash
pip install pillow
python tools/make_images.py
```

## Bilgileri güncelleme

| Ne değişecek | Nerede |
| --- | --- |
| Telefon, adres, saatler, bölgeler | `tools/site_data.py` içinde `BUSINESS` ve `templates/` |
| WhatsApp numarası (arıza bulucu) | `assets/js/main.js` içinde `PHONE_WA` |
| Hizmetler ve hizmet sayfası metinleri | `tools/site_data.py` içinde `SERVICES` |
| Ana sayfa SSS | `tools/site_data.py` içinde `HOME_FAQ` |
| Belirtiler ve olası arızalar | `assets/js/main.js` içinde `SYMPTOMS` ve `CAUSES` |
| Renkler ve yazı tipleri | `assets/css/style.css` en üstteki `:root` |
| Site adresi (alan adı) | `tools/site_data.py` içinde `BASE_URL` |

Yeni bir hizmet sayfası eklemek için `SERVICES` listesine bir kayıt ekleyip `python tools/build.py` çalıştırmak yeterlidir. Menü, alt bilgi, site haritası ve "Diğer hizmetler" listesi kendiliğinden güncellenir.

### Arıza bulucu nasıl çalışır

`CAUSES` listesindeki her arızanın, belirtilere göre puanları vardır (`w`). Müşterinin seçtiği belirtilerin puanları toplanır ve en yüksek puanlı arıza gösterilir. Dizel araçlarda DPF puanı artırılır, benzinli araçlarda azaltılır. Sonuçtaki "Yapılacak iş" ilgili hizmet sayfasına bağlanır.

```js
{ name: "Arıza adı", w: { ses: 3, koku: 2 }, urg: "mid", svc: "Yapılacak iş", page: "egzoz-tamiri", why: "Kısa açıklama." }
```

`urg` değeri `high` (acil), `mid` (orta) veya `low` (düşük) olabilir.

> Arıza bulucu yalnızca bir ön tahmindir. Kesin teşhis için araç dükkânda kontrol edilir.

## Arama motorları (SEO)

Sitenin Google'da "Esenyurt egzoz", "Esenyurt DPF temizliği" gibi aramalarda çıkması için:

- Her sayfanın kendine ait başlığı, açıklaması ve kalıcı adresi (`canonical`) var.
- Her hizmetin ayrı bir sayfası var. Google her sayfayı ayrı bir arama sonucu olarak gösterebilir.
- `sitemap.xml` tüm sayfaları listeler, `robots.txt` site haritasını gösterir.
- schema.org yapısal verisi Google'a işletmenin adını, adresini, telefonunu, saatlerini, hizmetlerini ve SSS'lerini bildirir.

Site sahibinin yapması gerekenler:

1. **Google İşletme Profili** açmak: [business.google.com](https://business.google.com). Haritada ve "yakınımdaki egzozcu" aramalarında çıkmanın en etkili yolu budur. Profilde site adresi olarak bu site girilir.
2. **Google Search Console**'a siteyi eklemek: [search.google.com/search-console](https://search.google.com/search-console). Site doğrulandıktan sonra `sitemap.xml` gönderilir.
3. Müşterilerden Google'da yorum istemek.

## Yayınlama

Site, `main` dalından **GitHub Pages** ile yayınlanır. `main` dalına gönderilen her değişiklik birkaç dakika içinde canlı siteye yansır.

Kendi alan adını (ör. `gumushanelileregzoz.com`) bağlamak için:

1. Alan adı satın alınır ve DNS ayarlarından GitHub Pages'e yönlendirilir.
2. Depoya alan adını içeren bir `CNAME` dosyası eklenir.
3. `tools/site_data.py` içindeki `BASE_URL` yeni adresle değiştirilir ve `python tools/build.py` çalıştırılır.

## Yol haritası

- [x] Arıza bulucu ve WhatsApp'a hazır mesaj
- [x] Kartvizitteki kimliğe uygun kurumsal tasarım
- [x] SEO etiketleri ve yapısal veri
- [x] Her hizmet için ayrı sayfa, site haritası ve paylaşım görseli
- [ ] Dükkânın ve yapılan işlerin gerçek fotoğrafları
- [ ] Google İşletme Profili ve harita konumu
- [ ] Google Search Console kaydı
- [ ] Kendi alan adı
- [ ] Müşteri yorumları
- [ ] Serbest yazıyla arıza tarifi (yapay zekâ desteği)

## İletişim

**Gümüşhaneliler Egzoz**
Fatih Oto Sanayi Sitesi C6 Blok No:6, Esenyurt / İstanbul
Erdal Albayrak: 0537 463 88 38 · Dükkân: 0212 690 32 18
Pazartesi–Cumartesi 09:00–19:00

---

<sub>© Gümüşhaneliler Egzoz. Tüm hakları saklıdır.</sub>
