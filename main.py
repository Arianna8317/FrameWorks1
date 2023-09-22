from flask import Flask, render_template


app = Flask(__name__)

@app.get('/main/')
def main():
    context = {"title": "Главная"}
    return render_template("main.html", **context)


@app.get('/clothes/')
def clothes():
    context = {"title": "Одежда"}
    return render_template("clothes.html", **context)


@app.get('/shoes/')
def shoes():
    context = {"title": "Обувь"}
    return render_template("shoes.html", **context)


@app.get('/coats/')
def coats():
    context = {"title": "Верхняя одежда"}
    return render_template("coats.html", **context)


if __name__ == '__main__':
    app.run()