from flask import Flask, request, render_template
import cv2
import os
import text_XOR_embedding
import img_embedding


app = Flask(__name__)
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
app.config['UPLOAD_FOLDER'] = desktop


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


@app.route('/textEncoding', methods=['GET', 'POST'])
def txtEncode():
    txt = request.form['text']
    imgFile = request.files['image']
    filename = 'TextCover.png'
    imgFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    url = desktop+filename
    img = cv2.imread(url, 1)
    text_XOR_embedding.encodeData(img, txt)
    return render_template("stegotext.html")


@app.route('/textDecoding', methods=['GET', 'POST'])
def txtDecode():
    imgFile = request.files['image']
    filename = 'TextStego.png'
    imgFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    url = desktop+filename
    img = cv2.imread(url, 1)
    data = text_XOR_embedding.decodeData(img)
    return 'Encoded Data:' + data


@app.route('/imageEncoding', methods=['GET', 'POST'])
def imgEncode():
    cover = request.files['coverImage']
    watermark = request.files['watermarkImage']

    cover.save(os.path.join(app.config['UPLOAD_FOLDER'], 'ImageCover.png'))
    watermark.save(os.path.join(
        app.config['UPLOAD_FOLDER'], 'ImageWatermark.png'))

    urlCover = desktop + 'ImageCover.png'
    urlWatermark = desktop + 'ImageWatermark.png'

    c = cv2.imread(urlCover, 1)
    w = cv2.imread(urlWatermark, 1)
    img_embedding.merge(w, c)
    return render_template("stegoimg.html")


@app.route('/imageDecoding', methods=['GET', 'POST'])
def imgDecode():
    stego = request.files['stegoImage']
    stego.save(os.path.join(app.config['UPLOAD_FOLDER'], 'ImageStego.png'))
    urlStego = desktop + 'ImageStego.png'
    s = cv2.imread(urlStego, 1)
    img_embedding.unmerge(s)
    return render_template("stegoimg.html")


if __name__ == "__main__":
    app.run(debug=True)
