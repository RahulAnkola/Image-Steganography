from flask import Flask, request, render_template
import cv2

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


@app.route('/textEncoding',methods=['GET', 'POST'])
def txtEncode():
    txt=request.form['text']
    url=request.form['image']
    img=cv2.imread(url,1)


if __name__ == "__main__":
    app.run(debug=True)
