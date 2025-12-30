# ContentFlow AI - SaaS Churn Analizi ve Tahminleme

Bu proje, **Quantex** ekibi tarafından "Üretken Yapay Zeka" dersi kapsamında geliştirilen, küçük işletmeler için sosyal medya içerik üretimini otomatize eden **ContentFlow AI** platformunun müşteri kaybını (churn) analiz etmek amacıyla oluşturulmuştur.

## 🚀 Proje Hakkında
**ContentFlow AI**, üretken yapay zeka kullanarak işletmelerin dijital varlıklarını yöneten bir SaaS platformudur. Bu analiz, kullanıcı davranışlarını inceleyerek platformu terk etme eğilimi olan müşterileri önceden tespit etmeyi ve elde tutma (retention) stratejileri geliştirmeyi amaçlar.

## 👥 Ekip (Quantex)
* **Enes Doğruk** - Yönetim Bilişim Sistemleri (YBS) 3. Sınıf Öğrencisi
* **Mehmet Efe Sağlık** - Proje Ortağı

## 📊 Veri Seti ve Metodoloji
Analiz sürecinde 5.000 satırlık sentetik müşteri verisi kullanılmıştır. Çalışma boyunca veri bilimi dünyasında standart olan **CRISP-DM** (Cross-Industry Standard Process for Data Mining) metodolojisi takip edilmiştir.

### Churn Mantığı (Business Logic)
Müşterilerin platformu terk etme olasılığı ($P$), aşağıdaki rasyonel kurallara ve olasılıksal dağılıma göre modellenmiştir:

$$P(\text{Churn}) = \begin{cases} 0.85, & \text{Müşteri\_Memnuniyeti} < 4 \text{ veya } \text{Aylık\_İçerik} < 10 \\ 0.05, & \text{Diğer durumlar} \end{cases}$$

## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python
* **Veri Analizi:** Pandas, NumPy
* **Görselleştirme:** Seaborn, Matplotlib
* **Versiyon Kontrol:** Git & GitHub (Profesyonel Git hijyeni ve `.gitignore` filtrelemesi uygulanmıştır)

## 📂 Dosya Yapısı
* `analiz.ipynb`: Veri keşfi (EDA) ve churn lojistiği uygulamalarını içerir.
* `app.py`: Platformun uygulama mantığını içeren temel kod dosyası.
* `.gitignore`: Veri setleri (`.csv`) ve model dosyalarının (`.pkl`) güvenliğini sağlayan yapılandırma.
