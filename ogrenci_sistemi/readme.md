 Öğrenci Bilgi Sistemi

 Geliştirici Bilgileri
 Ad Soyad: Tahir Kayar
 Öğrenci No: 2411081026

 Proje Hakkında
 Bu proje, öğrenci bilgilerini ve ders notlarını yönetmek için geliştirilen basit bir Flask web uygulamasıdır. Kullanıcılar sisteme giriş yaptıktan sonra öğrenci ekleme, not girme, düzenleme, silme ve listeleme işlemlerini gerçekleştirebilir.

 Amaç
 Projeyi geliştirme amacım; web tabanlı bir bilgi sisteminin temel işleyişini kavramak, kullanıcı kayıt sistemi ve veritabanı etkileşimlerini öğrenmekti. Aynı zamanda Flask çatısı ile temel CRUD işlemlerini uygulamalı olarak gerçekleştirdim.

 Kullanılan Teknolojiler
 Bileşen	Açıklama
 Backend	Python (Flask Framework)
 Veritabanı	SQLite
 Frontend	HTML, CSS (Bootstrap)
 Güvenlik	SHA256 ile parola şifreleme (Werkzeug)
 Oturum Yönetimi	Flask-Login
 Veri Dışa Aktarımı	JSON formatı ile kullanıcı verileri

 Özellikler
 Kullanıcı kayıt ve giriş sistemi (authentication)

 Öğrenci bilgileri ekleme, düzenleme, silme

 Not girişi (vize + final)

 Ortalama hesaplama ve geçme/kalma durumu

 JSON dosyasına veri aktarımı (users.json)

 Admin panel (dashboard) görünümü

 Şık ve sade kullanıcı arayüzü

 Kurulum Talimatları
 Gerekli kütüphaneleri yükleyin:pip install -r requirements.txt
 Uygulamayı çalıştırın:python app.py
 Tarayıcınızdan http://127.0.0.1:5000 adresine gidin.

## 📸 Ekran Görselleri

### 🔐 Giriş Sayfası
![Giriş Sayfası](screenshots/login.png)

### 📝 Kayıt Sayfası
![Kayıt Sayfası](screenshots/register.png)

### 🧭 Dashboard
![Dashboard](screenshots/dashboard.png)

### 📋 Öğrenci Listesi
![Öğrenci Listesi](screenshots/ogrenci_listesi.png)

### ✍️ Not Girişi
![Not Girişi](screenshots/not_girisi.png)

### 📊 Not Listesi
![Not Listesi](screenshots/not_listesi.png)


 📦 Veritabanı JSON Yedeği
 users.json dosyasıyla kayıtlı kullanıcı verileri dışa aktarılmıştır.

 öğrenci_sistemi/
 ├── app.py # Ana Python uygulama dosyası
 ├── templates/ # HTML şablonlarının bulunduğu klasör
 │ ├── index.html # Anasayfa
 │ ├── login.html # Giriş formu
 │ ├── register.html # Kayıt formu
 │ ├── dashboard.html # Kullanıcı kontrol paneli
 │ ├── ogrenci_ekle.html # Öğrenci ekleme formu
 │ ├── ogrenci_listesi.html # Öğrenci listeleme
 │ ├── ogrenci_duzenle.html # Öğrenci düzenleme
 │ ├── not_girisi.html # Not girişi formu
 │ └── not_listesi.html # Not listeleme
 ├── users.json # JSON yedeği (kullanıcılar)
 ├── requirements.txt # Gerekli Python paketleri
 └── README.md # Proje açıklama dosyası

https://flask-ogrenci-bilgi-sistemi-2.onrender.com

