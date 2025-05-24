from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gelistirme_anahtari'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Giriş sistemi
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Kullanıcı modeli
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Öğrenci modeli
class Ogrenci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100), nullable=False)
    soyad = db.Column(db.String(100), nullable=False)
    numara = db.Column(db.String(20), nullable=False)
    sinif = db.Column(db.String(20), nullable=False)

# Not modeli
class Not(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ogrenci_no = db.Column(db.String(20), nullable=False)
    ders = db.Column(db.String(100), nullable=False)
    vize = db.Column(db.Integer, nullable=False)
    final = db.Column(db.Integer, nullable=False)

# Anasayfa
@app.route("/")
def index():
    return render_template("index.html")

# Giriş
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Giriş başarılı!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Geçersiz e-posta veya şifre', 'danger')
            return redirect(url_for('login'))

    return render_template("login.html")

# Kayıt
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        if User.query.filter_by(email=email).first():
            flash('Bu e-posta zaten kayıtlı!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Kayıt başarılı! Giriş yapabilirsiniz.', 'success')
        return redirect(url_for('login'))

    return render_template("register.html")

# Dashboard
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", name=current_user.name)

# Çıkış
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

# Öğrenci Ekle
@app.route("/ogrenci_ekle", methods=["GET", "POST"])
def ogrenci_ekle():
    if request.method == "POST":
        ad = request.form.get("ad")
        soyad = request.form.get("soyad")
        numara = request.form.get("numara")
        sinif = request.form.get("sinif")

        yeni = Ogrenci(ad=ad, soyad=soyad, numara=numara, sinif=sinif)
        db.session.add(yeni)
        db.session.commit()

        flash("Öğrenci başarıyla eklendi!", "success")
        return redirect(url_for("ogrenci_listesi"))

    return render_template("ogrenci_ekle.html")

# Öğrenci Listesi
@app.route("/ogrenci_listesi")
def ogrenci_listesi():
    ogrenciler = Ogrenci.query.all()
    return render_template("ogrenci_listesi.html", ogrenciler=ogrenciler)

# Öğrenci Sil
@app.route("/ogrenci_sil/<int:id>")
def ogrenci_sil(id):
    ogrenci = Ogrenci.query.get_or_404(id)
    db.session.delete(ogrenci)
    db.session.commit()
    flash("Öğrenci silindi.", "success")
    return redirect(url_for("ogrenci_listesi"))

# Öğrenci Düzenle
@app.route("/ogrenci_duzenle/<int:id>", methods=["GET", "POST"])
def ogrenci_duzenle(id):
    ogrenci = Ogrenci.query.get_or_404(id)

    if request.method == "POST":
        ogrenci.ad = request.form.get("ad")
        ogrenci.soyad = request.form.get("soyad")
        ogrenci.numara = request.form.get("numara")
        ogrenci.sinif = request.form.get("sinif")
        db.session.commit()
        flash("Öğrenci güncellendi.", "success")
        return redirect(url_for("ogrenci_listesi"))

    return render_template("ogrenci_duzenle.html", ogrenci=ogrenci)

# Not Girişi
@app.route("/not_girisi", methods=["GET", "POST"])
def not_girisi():
    if request.method == "POST":
        ogrenci_no = request.form.get("ogrenci_no")
        ders = request.form.get("ders")
        vize = request.form.get("vize")
        final = request.form.get("final")

        print("GELEN VERİ:", ogrenci_no, ders, vize, final)

        if ogrenci_no and ders and vize and final:
            try:
                yeni_not = Not(
                    ogrenci_no=ogrenci_no,
                    ders=ders,
                    vize=int(vize),
                    final=int(final)
                )
                db.session.add(yeni_not)
                db.session.commit()
                flash("Not başarıyla kaydedildi.", "success")
            except Exception as e:
                print("KAYIT HATASI:", e)
                flash("Not kaydedilemedi!", "danger")
        else:
            flash("Tüm alanları doldurun!", "warning")

        return redirect(url_for("not_listesi"))

    return render_template("not_girisi.html")

# Not Listesi
@app.route("/not_listesi")
def not_listesi():
    notlar = Not.query.all()
    return render_template("not_listesi.html", notlar=notlar)

# Veritabanı oluşturma
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
