from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def default():
    return render_template("index.html")


@app.route('/stegoimg.html')
def stegoimg():
    return render_template("stegoimg.html")


@app.route('/stegotext.html')
def stegotext():
    return render_template("stegotext.html")


@app.route('/index.html')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
