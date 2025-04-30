from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/ogrenci_listesi")
def ogrenci_listesi():
    return render_template("ogrenci_listesi.html")

@app.route("/ogrenci_ekle")
def ogrenci_ekle():
    return render_template("ogrenci_ekle.html")

@app.route("/ogrenci_duzenle")
def ogrenci_duzenle():
    return render_template("ogrenci_duzenle.html")

@app.route("/not_girisi")
def not_girisi():
    return render_template("not_girisi.html")

if __name__ == "__main__":
    app.run(debug=True)
