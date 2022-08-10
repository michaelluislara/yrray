import os
import requests
from flask import Flask, render_template

cubes = requests.get('https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesListLite', stream=True)
cubelist = cubes.json()
newlist = []
for x in range(0,len(cubelist)):
  newlist.append(cubelist[x]['cubeTitleEn'])

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    # a simple page that says hello
    @app.route('/')
    def indexpage():
        return render_template(
        "index.html"
    )
    
    @app.route('/base')
    def basepage():
        return render_template(
        "base.html"
    )
    
    @app.route('/dashboardlist')
    def dashboardpage():
        return render_template(
        "dashboardlist.html",
        newlist=newlist
    )
    
    @app.route('/about')
    def aboutpage():
        return render_template(
        "about.html"
    )
    
    return app