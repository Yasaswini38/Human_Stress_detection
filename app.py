from flask import Flask, Response, render_template
from test2 import VideoCamera

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')



