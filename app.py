from flask import Flask, send_file
import qrcode
import PIL
from io import StringIO, BytesIO
# link = "https://www.youtube.com/"

# img = qrcode.make(link)
# img.save("test0.jpg")

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello! In order to get your desired QR Code, use '/{data}' route. Where {} indicates your data</h1>"

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/<path:suburl>')
def path(suburl):
    data = suburl
    img = qrcode.make(data)
    # img.save("test1.jpg")
    # return render_template('qr.html', data=data)
    return serve_pil_image(img)
    # return send_file(img, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)