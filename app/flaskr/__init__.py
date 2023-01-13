from flask import Flask, render_template, request
import requests
import os
import json


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=('GET', 'POST'))
    def getPost():
        if request.method == 'POST':
            try:
                title = request.form['title']
                data = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={title}").json()
                return render_template('test.html',data=data)
            except:
                return render_template('error.html')
        else:
            return render_template('home.html')
    return app