"""All site content: business details, service pages and FAQ.

Edit this file, then run `python tools/build.py` to regenerate the site.
Page copy is intentionally in Turkish (the site's audience).
"""

# Change this when a custom domain is set up (no trailing slash), e.g. "https://eralegzoz.com"
BASE_URL = "https://alikaganalbayrak.github.io/eral-egzoz"

BUSINESS = {
    "name": "ER AL Egzoz",
    "owners": "Erdoğan & Erdal Albayrak",
    "contact_person": "Erdal Albayrak",
    "gsm": "0537 463 88 38",
    "gsm_intl": "+905374638838",
    "landline": "0212 690 32 18",
    "landline_intl": "+902126903218",
    "whatsapp": "905374638838",
    "street": "Fatih Oto Sanayi Sitesi C6 Blok No:6",
    "district": "Esenyurt",
    "city": "İstanbul",
    "hours_text": "Pazartesi–Cumartesi 09:00–19:00",
    "maps": "https://www.google.com/maps/search/?api=1&query=Fatih+Oto+Sanayi+Sitesi+C6+Blok+Esenyurt+%C4%B0stanbul",
    "area_served": ["Esenyurt", "Beylikdüzü", "Avcılar", "Büyükçekmece", "Başakşehir", "İstanbul"],
}

ICONS = {
    "dpf": '<rect x="3" y="7" width="18" height="10" rx="3"/><path d="M8 7v10M12 7v10M16 7v10"/>',
    "kat": '<rect x="5" y="6" width="14" height="12" rx="4"/><path d="M2 12h3M19 12h3M9 10h6M9 14h6"/>',
    "degisim": '<path d="M3 12h11"/><rect x="13" y="8" width="8" height="8" rx="3"/><path d="M6 8 3 12l3 4"/>',
    "tamir": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4 2.6-2.6Z"/>',
    "kaynak": '<path d="m4 20 8-8"/><path d="m12 12 3-3 2 2-3 3z"/><path d="M18 3v2M21 6h-2M20 4l-1.2 1.2"/>',
    "cihaz": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/><path d="m7 11 2-2 2 3 2-4 2 3h2"/>',
}

# Each service gets its own page at /hizmetler/<slug>/
SERVICES = [
    {
        "slug": "dpf-temizligi",
        "icon": "dpf",
        "name": "DPF temizliği ve değişimi",
        "short": "Tıkanan partikül filtresini söküp temizliyor, gerekirse değiştiriyoruz.",
        "title": "Esenyurt DPF Temizliği ve Değişimi",
        "description": "Esenyurt Fatih Oto Sanayi Sitesi'nde DPF temizliği ve DPF değişimi. Güç kaybı, DPF uyarı lambası ve siyah duman sorunlarında cihazla kontrol. Hemen arayın: 0537 463 88 38.",
        "lead": "DPF lambanız yandı, aracınız çekmiyor mu? Tıkanan dizel partikül filtresini söküp temizliyor, temizlenemeyecek durumdaysa değiştiriyoruz.",
        "body": [
            "DPF (dizel partikül filtresi), dizel araçlarda egzozdan çıkan isi tutan filtredir. Araç normalde bu isi belirli aralıklarla yakarak filtreyi kendisi temizler. Ancak araç çoğunlukla şehir içinde, kısa mesafelerde kullanılıyorsa bu yakma işlemi tamamlanamaz ve filtre zamanla tıkanır.",
            "Tıkalı bir DPF ile yola devam etmek motorun nefes almasını zorlaştırır. Araç güç kaybeder, yakıt tüketimi artar ve uzun vadede turbo ile motor zarar görebilir. Bu yüzden DPF uyarısı yandığında aracı bekletmeden kontrol ettirmeniz önerilir.",
        ],
        "symptoms": ["DPF / partikül filtresi uyarı lambası", "Güç kaybı, aracın çekmemesi", "Motor arıza lambası", "Egzozdan siyah duman", "Yakıt tüketiminin artması", "Aracın acil durum (limp) moduna geçmesi"],
        "process": [
            ("Kontrol", "Cihazla arıza kodlarını okuyup filtrenin doluluğunu ve sensörleri kontrol ediyoruz."),
            ("Sökme", "DPF'yi egzoz hattından söküyoruz."),
            ("Temizlik", "Filtrenin içindeki is ve külü temizliyoruz. Filtre çatlak veya erimişse değişim öneriyoruz."),
            ("Montaj ve test", "Filtreyi yerine takıyor, arıza kodlarını silip aracı test ediyoruz."),
        ],
        "faq": [
            ("DPF temizliği mi, değişimi mi gerekir?", "Filtre sağlamsa temizlik çoğu zaman yeterlidir. İçi çatlamış veya erimişse temizlik işe yaramaz ve değişim gerekir. Aracı kontrol ettikten sonra hangisinin gerektiğini söylüyoruz."),
            ("DPF neden tekrar tıkanır?", "En sık sebep aracın uzun süre kısa mesafede kullanılmasıdır. Arızalı bir sensör, enjektör ya da EGR sorunu da filtrenin hızlı dolmasına yol açabilir. Kontrolde bunlara da bakıyoruz."),
            ("DPF temizliği fiyatı ne kadar?", "Fiyat aracın modeline ve filtrenin durumuna göre değişir. Arayın veya WhatsApp'tan araç bilgilerinizi yazın, size bilgi verelim."),
        ],
    },
    {
        "slug": "katalizator",
        "icon": "kat",
        "name": "Katalizatör temizliği ve değişimi",
        "short": "Muayeneden kalan, koku yapan veya güç düşüren katalizatörler.",
        "title": "Esenyurt Katalizatör Temizliği ve Değişimi",
        "description": "Esenyurt'ta katalizatör temizliği ve değişimi. Muayeneden emisyon yüzünden kalan, çürük yumurta kokusu yapan ve güç kaybettiren katalizatörler. ER AL Egzoz, Fatih Oto Sanayi.",
        "lead": "Aracınız muayeneden emisyon yüzünden mi kaldı, egzozdan çürük yumurta kokusu mu geliyor? Katalizatörü kontrol edip temizliyor veya değiştiriyoruz.",
        "body": [
            "Katalizatör (katalitik konvertör), egzoz gazındaki zararlı maddeleri daha az zararlı gazlara dönüştüren parçadır. Araç muayenesindeki emisyon testinden geçmek için katalizatörün düzgün çalışması gerekir.",
            "Zamanla katalizatörün içi tıkanabilir, eriyebilir veya parçalanabilir. Tıkalı katalizatör egzoz gazının çıkışını zorlaştırır ve güç kaybına yol açar. İçi dağılmış bir katalizatör ise egzozdan çıngırak sesi gelmesine neden olur.",
        ],
        "symptoms": ["Muayenede emisyon testinden kalma", "Çürük yumurta (kükürt) kokusu", "Güç kaybı ve hızlanmada zorlanma", "Egzozdan çıngırak, tıkırtı sesi", "Motor arıza lambası", "Yakıt tüketiminin artması"],
        "process": [
            ("Kontrol", "Cihazla arıza kodlarını ve oksijen sensörü değerlerini kontrol ediyoruz."),
            ("Tespit", "Katalizatörün tıkalı mı, kırık mı olduğunu belirliyoruz."),
            ("Temizlik veya değişim", "Temizlenebilecek durumdaysa temizliyor, değilse aracınıza uygun katalizatörle değiştiriyoruz."),
            ("Test", "Aracı çalıştırıp egzoz hattını ve arıza kodlarını tekrar kontrol ediyoruz."),
        ],
        "faq": [
            ("Muayeneden emisyon yüzünden kaldım, sebebi katalizatör mü?", "Çoğu zaman katalizatör veya oksijen sensörü kaynaklıdır. Aracı kontrol edip sebebini bulur, muayeneden geçmesi için gereken işlemi yaparız."),
            ("Katalizatör temizlenebilir mi?", "İçi tıkanmış ama sağlam olan katalizatörler temizlenebilir. İçi erimiş veya parçalanmışsa değişim gerekir."),
            ("Katalizatör fiyatı ne kadar?", "Aracın markasına ve modeline göre değişir. Arayın veya WhatsApp'tan yazın, araç bilgilerinize göre bilgi verelim."),
        ],
    },
    {
        "slug": "egzoz-degisimi",
        "icon": "degisim",
        "name": "Egzoz değişimi",
        "short": "Susturucu, ara boru ve arka egzoz değişimi. Orijinal Matay egzoz.",
        "title": "Esenyurt Egzoz Değişimi ve Susturucu",
        "description": "Esenyurt'ta egzoz değişimi: susturucu, ara boru, arka egzoz. Matay yetkili servisi, orijinal Matay egzoz. ER AL Egzoz, Fatih Oto Sanayi Sitesi C6 Blok.",
        "lead": "Delinen, çürüyen veya ses yapan egzozunuzu aracınıza uygun orijinal Matay egzozla değiştiriyoruz.",
        "body": [
            "Egzoz sistemi; manifold, katalizatör, ara boru, susturucular ve arka egzozdan oluşur. Yol tuzu, nem ve ısı nedeniyle bu parçalar zamanla paslanır ve delinir. Delik bir susturucu aracın sesini artırır, egzoz gazının araç içine girmesine de yol açabilir.",
            "Matay yetkili servisi olarak aracınızın modeline uygun orijinal Matay egzoz parçaları kullanıyoruz. Sadece arızalı parçayı değiştiriyor, sağlam parçalara dokunmuyoruz.",
        ],
        "symptoms": ["Egzoz sesinin artması", "Susturucuda pas veya delik", "Araç içine egzoz kokusu gelmesi", "Egzozun sarkması veya yere sürtmesi", "Alttan tıkırtı sesi"],
        "process": [
            ("Kontrol", "Aracı kaldırıp egzoz hattının tamamını kontrol ediyoruz."),
            ("Bilgi ve fiyat", "Hangi parçanın değişmesi gerektiğini ve fiyatı söylüyoruz."),
            ("Değişim", "Arızalı parçayı söküp aracınıza uygun yeni parçayı takıyoruz."),
            ("Test", "Bağlantıları ve askıları kontrol edip kaçak olmadığından emin oluyoruz."),
        ],
        "faq": [
            ("Egzozun tamamını mı değiştirmek gerekir?", "Genellikle hayır. Sadece delinen veya çürüyen parça değiştirilir. Kontrol ettikten sonra neyin değişmesi gerektiğini söylüyoruz."),
            ("Hangi marka egzoz kullanıyorsunuz?", "Matay yetkili servisiyiz. Aracınıza uygun orijinal Matay egzoz parçaları kullanıyoruz."),
            ("Egzoz değişimi fiyatı ne kadar?", "Aracın modeline ve değişecek parçaya göre değişir. Arayın veya WhatsApp'tan yazın."),
        ],
    },
    {
        "slug": "egzoz-tamiri",
        "icon": "tamir",
        "name": "Egzoz tamiri",
        "short": "Delinen, çatlayan egzozların ve kopan askıların tamiri.",
        "title": "Esenyurt Egzoz Tamiri",
        "description": "Esenyurt'ta egzoz tamiri: delik, çatlak, kopan egzoz askısı, gaz kaçağı ve egzoz sesi. ER AL Egzoz, Fatih Oto Sanayi Sitesi. Hemen arayın: 0537 463 88 38.",
        "lead": "Egzozunuz ses mi yapıyor, sarktı mı, araç içine koku mu geliyor? Değişim gerektirmeyen arızaları tamir ediyoruz.",
        "body": [
            "Her egzoz arızası parça değişimi gerektirmez. Küçük delikler, çatlaklar, gevşeyen kelepçeler ve kopan lastik askılar tamir edilerek egzoz sağlıklı şekilde kullanılmaya devam edebilir.",
            "Egzozdan gelen gaz kaçağını hafife almayın. Kaçan egzoz gazı araç içine girebilir ve karbonmonoksit zehirlenmesine yol açabilir. Sarkan bir egzoz ise yolda kopup düşebilir.",
        ],
        "symptoms": ["Egzoz sesinin artması", "Egzozun sarkması veya sürtmesi", "Alttan tıkırtı veya takırtı sesi", "Araç içine egzoz kokusu gelmesi", "Bağlantı yerlerinde is izi"],
        "process": [
            ("Kontrol", "Aracı kaldırıp kaçak, çatlak ve askıları kontrol ediyoruz."),
            ("Bilgi ve fiyat", "Tamirin yeterli olup olmadığını ve fiyatı söylüyoruz."),
            ("Tamir", "Kaynak, conta, kelepçe veya askı değişimiyle arızayı gideriyoruz."),
            ("Test", "Motoru çalıştırıp kaçak kalmadığını kontrol ediyoruz."),
        ],
        "faq": [
            ("Egzoz sesi arttı, ne yapmalıyım?", "Ses artışı genellikle delik bir susturucu veya bağlantı yerindeki kaçaktan olur. Araç içine koku da geliyorsa beklemeden getirin."),
            ("Egzoz askısı koptu, aracı kullanabilir miyim?", "Kısa mesafede dikkatlice gelebilirsiniz ama uzun yol yapmayın. Sarkan egzoz yolda kopabilir."),
            ("Tamir mi, değişim mi daha iyi?", "Parça sağlamsa tamir yeterlidir. Çok paslanmış veya çürümüşse değişim daha uzun ömürlü olur. Gördükten sonra size öneriyoruz."),
        ],
    },
    {
        "slug": "egzoz-kaynak",
        "icon": "kaynak",
        "name": "Egzoz kaynağı",
        "short": "Egzoz borusu, manifold ve bağlantı noktalarında kaynak işleri.",
        "title": "Esenyurt Egzoz Kaynağı ve Manifold Kaynağı",
        "description": "Esenyurt'ta egzoz kaynağı: egzoz borusu, manifold çatlağı ve bağlantı noktaları. ER AL Egzoz, Fatih Oto Sanayi Sitesi C6 Blok No:6.",
        "lead": "Çatlayan manifold, delinen boru ya da kopan bağlantı. Egzoz hattındaki kaynak işlerini dükkânımızda yapıyoruz.",
        "body": [
            "Egzoz hattı sürekli ısınıp soğuduğu ve titreştiği için zamanla borularda ve bağlantı noktalarında çatlaklar oluşur. Bu çatlaklar ses ve gaz kaçağına yol açar.",
            "Manifold çatlakları genellikle motor soğukken tıkırtı sesiyle kendini belli eder, motor ısınınca ses azalır. Bu tür arızaları ve boru bağlantılarını kaynakla onarıyoruz.",
        ],
        "symptoms": ["Motor soğukken tıkırtı, ısınınca azalan ses", "Boru veya bağlantıda çatlak", "Egzoz sesinin artması", "Motor bölümünden egzoz kokusu"],
        "process": [
            ("Kontrol", "Çatlak veya kopuk olan yeri tespit ediyoruz."),
            ("Hazırlık", "Kaynak yapılacak yüzeyi pas ve kirden temizliyoruz."),
            ("Kaynak", "Çatlağı veya bağlantıyı kaynakla onarıyoruz."),
            ("Test", "Motoru çalıştırıp kaçak olup olmadığını kontrol ediyoruz."),
        ],
        "faq": [
            ("Manifold çatlağı kaynakla onarılır mı?", "Çatlağın yerine ve büyüklüğüne bağlıdır. Çoğu durumda kaynakla onarılabilir. Kontrol ettikten sonra söylüyoruz."),
            ("Kaynak yapılan yer tekrar çatlar mı?", "Doğru yapılan kaynak uzun süre dayanır. Parça çok çürümüşse kaynak yerine değişim öneriyoruz."),
            ("Kaynak fiyatı ne kadar?", "İşin büyüklüğüne göre değişir. Arayın veya fotoğraf çekip WhatsApp'tan gönderin."),
        ],
    },
    {
        "slug": "ariza-kontrolu",
        "icon": "cihaz",
        "name": "Arıza kontrolü",
        "short": "Cihazla arıza kodu okuma, sensör ve egzoz hattı kontrolü.",
        "title": "Esenyurt Egzoz Arıza Kontrolü ve Arıza Tespiti",
        "description": "Esenyurt'ta cihazla egzoz arıza tespiti: arıza kodu okuma, oksijen ve DPF fark basınç sensörü kontrolü. ER AL Egzoz, Fatih Oto Sanayi Sitesi.",
        "lead": "Arıza lambası yandı ama sebebini bilmiyor musunuz? Cihazla arıza kodlarını okuyup sorunun egzozdan mı başka bir yerden mi geldiğini buluyoruz.",
        "body": [
            "Motor arıza lambası çok farklı sebeplerle yanabilir. Egzoz hattındaki oksijen sensörü, DPF fark basınç sensörü veya katalizatör arızaları bu sebeplerin başında gelir.",
            "Tahminle parça değiştirmek hem zaman hem para kaybıdır. Cihazla arıza kodlarını okuyarak sorunu doğru tespit ediyor, sonra size ne yapılması gerektiğini söylüyoruz. Sorun egzoz dışından geliyorsa sizi doğru yere yönlendiriyoruz.",
        ],
        "symptoms": ["Motor arıza lambası", "DPF uyarı lambası", "Yakıt tüketiminin artması", "Güç kaybı", "Muayeneden emisyon yüzünden kalma"],
        "process": [
            ("Cihaza bağlama", "Aracınızı arıza tespit cihazına bağlıyoruz."),
            ("Kod okuma", "Kayıtlı arıza kodlarını ve sensör değerlerini okuyoruz."),
            ("Fiziki kontrol", "Egzoz hattını ve ilgili sensörleri kontrol ediyoruz."),
            ("Bilgilendirme", "Sorunu ve yapılması gerekeni size anlatıyoruz."),
        ],
        "faq": [
            ("Arıza lambası yanıyorsa araç kullanılır mı?", "Lamba sabit yanıyorsa kısa sürede kontrol ettirin. Yanıp sönüyorsa veya araç güç kaybediyorsa kullanmamanız daha doğru olur."),
            ("Arıza kodunu silmek sorunu çözer mi?", "Hayır. Kod silinse bile sorun devam ediyorsa lamba tekrar yanar. Önce sebebi bulmak gerekir."),
            ("Sorun egzozdan değilse ne oluyor?", "Cihazla sorunun nereden geldiğini görüyoruz. Egzozla ilgili değilse size söyler, doğru yere yönlendiririz."),
        ],
    },
]

HOME_FAQ = [
    ("DPF neden tıkanır?", "DPF, dizel araçlarda egzozdaki isi tutan filtredir. Araç çoğunlukla şehir içinde kısa mesafe kullanılıyorsa filtre kendini temizleyemez ve zamanla tıkanır. Güç kaybı ve DPF uyarı lambası en sık görülen belirtilerdir."),
    ("DPF temizliği mi, değişimi mi gerekir?", "Filtre sağlamsa temizlik çoğu zaman yeterlidir. İçi çatlamış veya erimişse değişim gerekir. Aracı görüp kontrol ettikten sonra hangisinin gerektiğini söyleriz."),
    ("Aracım muayeneden emisyon yüzünden kaldı, ne yapmalıyım?", "Genellikle katalizatör ya da egzoz sensörü kaynaklıdır. Katalizatörü kontrol edip temizlik veya değişimle aracınızın tekrar muayeneden geçmesini sağlarız."),
    ("Fiyat ne kadar?", "Fiyat aracın markasına, modeline ve sorunun ne olduğuna göre değişir. Arayın veya WhatsApp'tan yazın. Aracı gördükten sonra net fiyat veririz."),
    ("Randevu almam gerekiyor mu?", "Pazartesiden cumartesiye 09:00–19:00 arası doğrudan gelebilirsiniz. Önceden arar ya da yazarsanız beklemeden işlem yaparız."),
    ("Dükkânınız nerede?", "Esenyurt Fatih Oto Sanayi Sitesi C6 Blok No:6'dayız. Beylikdüzü, Avcılar, Büyükçekmece ve Bahçeşehir'e yakınız. Sayfanın altındaki Yol Tarifi Al butonuyla haritada açabilirsiniz."),
]
