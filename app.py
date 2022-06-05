import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd

import flask_cors
from flask import Flask, flash, request, redirect, url_for, session, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

import predict
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')



UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
PATH_TO_MODEL="Utils/model-3x3.h5"



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/try')
def tryy():
    return render_template('try.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    print("here is the request body",request)
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response=predict.get_predictions(PATH_TO_MODEL, destination)
    return render_template('results.html', data=response)
PATH_TO_MODEL="Utils/model-3x3.h5"

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=True)

flask_cors.CORS(app, expose_headers='Authorization')