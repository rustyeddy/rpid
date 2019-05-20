#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import Response

from flask_bootstrap import Bootstrap

from multiprocessing import Process
from multiprocessing import Queue

# from motor import Skidder

# from cam import controlled_image_server_behavior
# from cam import frame_generator
import time

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # return render_template('index.html', title="Mobile Robot I/O")
    return render_template(display_template)

@app.route('/hello')
def hello_world():
    return render_template('index.html')

@app.route('/camera/snap')
def snap_shot():
    ## TODO: take snapshot here
    return render_template('snap_shot.html')

@app.route("/image")
def image_server():
    return render_template('image_server.html')
    
@app.route("/display")
def display():
    return Response(frame_generator(),
            mimetype='multipart/x-mixed-replace; boundary=frame')

import time
def start_server_process(template_name):
    """Start the process, call terminate to close it"""
    global display_template

    display_template = template_name

    server = Process(target=app.run, kwargs={"host": "0.0.0.0", "port": 5001})
    server.start()
    return server

# app.run(host="0.0.0.0", debug=True, port=5001)
# process = start_server_process('control_image_behavior.html')
