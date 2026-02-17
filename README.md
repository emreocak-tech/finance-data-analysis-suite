🌍 Kapsamlı Veri Analiz ve Otomasyon Sistemi
Bu proje, borsa analizi, ülke GDP analizi, araç veri analizi, Trendyol ürün takibi, döviz kuru hesaplama ve veritabanı işlemlerini tek bir çatı altında toplayan çok modüllü bir Python uygulamasıdır.

🚀 Özellikler
📈 Borsa Analiz Modülü (stockmarket.py)
Hisse Senedi Analizi: Yahoo Finance verileriyle hisse analizi

Prophet Tahmini: Facebook Prophet ile gelecek tahmini

Hacim Grafikleri: İşlem hacmi görselleştirme

Çoklu Hisse Karşılaştırma: 3 farklı hisseyi karşılaştırma

🌍 Ülke GDP Analizi (country_data.py)
GDP Sıralaması: 2025 yılına göre en yüksek 10 ülke GDP'si

Ülke Bazlı Analiz: Seçilen ülkenin yıllara göre GDP değerleri

Büyüme Hesaplama: Yıllık ortalama büyüme yüzdesi

GDP Tahmini: Linear Regression ile 2026 GDP tahmini

🚗 Araç Veri Analizi (cars.py)
Marka Bazlı Analiz: BMW, Ford, Porsche, Toyota, VW araç sayıları

Araç Seçimi: Marka ve modele göre araç detayları

Fiyat Analizi: Motor hacmi-fiyat, kilometre-fiyat ilişkisi

Fiyat Tahmini: Yıl ve kilometreye göre fiyat tahmini

🛒 Trendyol Otomasyonu (trendyol_scraping.py)
Ürün Çekme: BeautifulSoup ile Trendyol'dan ürün verisi çekme

MySQL Kayıt: Ürün bilgilerini veritabanına kaydetme

Telegram Bildirim: Çekilen ürünleri Telegram'a gönderme

Grafik Oluşturma: Ürün fiyatlarına göre bar grafiği

💱 Döviz Kuru Modülü
Dolar/TL: Anlık dolar kuru ve TL hesaplama

Euro/TL: Anlık euro kuru ve TL hesaplama

ExchangeRate-API: Güncel kur bilgisi

📱 PyQt5 Uygulama
Borsa Kayıt Arayüzü: Şirket adı, kodu ve fiyat bilgisi girişi

MySQL Kayıt: Kullanıcı verilerini veritabanına kaydetme

Sözleşme Onayı: Kullanıcı sözleşmesi kontrolü

📁 Gereksinimler
bash
pip install pandas numpy matplotlib scikit-learn yfinance prophet mysql-connector-python requests beautifulsoup4 selenium PyQt5 python-dotenv networkx
🔧 Kurulum
Projeyi klonlayın

.env dosyası oluşturun:

env
my_csv_path=arac_verileri.csv
host=localhost
user=root
password=your_password
database=your_db
exchange_rate_api=your_api_key
url_information=url1,url2,url3
apı_key=telegram_bot_api
chat_id=telegram_chat_id
password2=db_password2
host2=localhost2
database2=db2
user2=root2
Gerekli CSV dosyalarını hazırlayın

Programı çalıştırın:

bash
python main.py
📂 Dosya Yapısı
main.py - Ana menü ve yönlendirme

stockmarket.py - Borsa analiz modülü

country_data.py - Ülke GDP analiz modülü

cars.py - Araç veri analiz modülü

trendyol_scraping.py - Trendyol otomasyon modülü

.env - API anahtarları ve konfigürasyon

🎯 Kullanım
Program çalıştırıldığında 17 farklı işlem sunar:

text
Welcome
You can:
1=StockMarket Analyze
2=Make a Predict about StockMarket
3=Analyze GDP
4=Research GDP for per country
5=Make a Predict about GDP
6=Cars Analyze
7=Read information about Cars
8=Make a Predict about price of cars
9=Show Product
10=Record your products due to MySql
11=Get Your products due to MySql
12=Send a message for Telegram
13=Create A Image about price pf products
14=Dolar
15=Euro
16=App
17=Quit on system
📊 Veri Setleri
Araç Verileri (cars.py)
Sütunlar: Manufacturer, Model, Price, Mileage, Engine size, Year of manufacture

GDP Verileri (country_data.py)
Sütunlar: Country, 2020, 2021, 2022, 2023, 2024, 2025

Borsa Verileri (stockmarket.py)
Yahoo Finance API üzerinden canlı veri

🧠 Sınıf Hiyerarşisi
Abstract Base Classes
CountryData (GDP analizleri için)

Cars (araç analizleri için)

Product (Trendyol ürünleri için)

DatasforStockMarket (borsa analizleri için)

Alt Sınıflar
AnalyzeGdp, GdpGrow, PredictGdp

AnalyzeCars, SimulationCars, MakePredictCars

TrendyolScraping, MySqlSave, MySqlSort, Telegram, CreateImage

Analyze, MakePredict

📈 Tahmin Modelleri
Linear Regression
GDP tahmini (yıllara göre)

Araç fiyat tahmini (yıl ve kilometreye göre)

Facebook Prophet
Borsa fiyat tahmini

Hacim tahmini

💾 Veritabanı İşlemleri
MySQL Tabloları
sql
-- Trendyol ürünleri
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price VARCHAR(50)
);

-- Borsa kayıtları
CREATE TABLE new_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    code VARCHAR(50),
    price DECIMAL(10,2),
    time DATETIME
);
🤖 Telegram Bot Entegrasyonu
Çekilen ürünler Telegram'a gönderilir

Ürün adı ve fiyat bilgisi

Otomatik mesaj gönderimi

📊 Grafik Türleri
Borsa Hacim Grafiği: Zaman serisi + ortalama çizgisi

GDP Bar Grafiği: En yüksek 10 ülke + ortalama çizgisi

Araç Sayı Grafiği: Marka bazlı araç sayıları

Scatter Plot: Motor hacmi-fiyat, kilometre-fiyat ilişkisi

Prophet Grafikleri: Tahmin görselleştirme

Trendyol Bar Grafiği: Ürün fiyatları

🖥️ PyQt5 Arayüzü
BasicApp sınıfı ile:

Şirket adı, kodu ve fiyat girişi

Kullanıcı sözleşmesi onayı

MySQL veritabanına kayıt

Hata yönetimi ve bilgi mesajları

🔗 API'ler
Yahoo Finance: Borsa verileri

ExchangeRate-API: Döviz kurları

Telegram Bot API: Mesaj gönderimi

⚠️ Hata Yönetimi
Her modülde try-except blokları ile:

Bağlantı hataları

Veritabanı hataları

Kullanıcı giriş hataları

API hataları

🔒 Encapsulation
Private attribute: __df, __headers, __url

Protected attribute: _name, _price, _df, _starttime, _endtime

Getter metotları: get_name(), get_price(), get_df()
