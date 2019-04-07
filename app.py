from flask import Flask
from flask import render_template
from flask import Response
import camera
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Mobile Robot I/O")

@app.route('/hello')
def hello_world():
    return render_template('index.html')

@app.route('/routes')
def display_routes():
    print(url_for('index'))
    print(url_for('login'))

@app.route("/image")
def image_server():
    return render_template('image_server.html')
    
@app.route("/display")
def display():
    return Response(camera.frame_generator(),
            mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host="0.0.0.0", debug=True, port=5001)
