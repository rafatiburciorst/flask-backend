from flask import Flask, render_template, jsonify, Response
from flask_cors import CORS
from fpv.cam import gen_frames

app:Flask = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return jsonify({'test': 'test'})

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')