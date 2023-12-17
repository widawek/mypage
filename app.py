from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("me")


@app.route("/me")
def me():
    content = {
        "title": "O mnie",
        "name": "Dawid",
        "surname": "Okrojek"
    }
    main_title = "informacje o mnie"
    return render_template("me.html", content=content, main_title=main_title)


@app.route("/contact")
def contact():
    content = {
        "title": "Kontakt",
        "email": "email: dawid.okrojek@gmail.com",
        "phone": "telefon: 700-600-500"
    }
    main_title = "informacje kontaktowe i zapis formularza"
    return render_template("contact.html", content=content,
                           main_title=main_title)


if __name__ == "__main__":
    app.run(debug=True)
