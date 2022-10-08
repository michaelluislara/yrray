import os
import requests
from flask import Flask, render_template, request, url_for, flash, redirect
cubes = requests.get('https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesListLite', stream=True)
cubelist = cubes.json()
cubelist = sorted(cubelist, key=lambda d: d['cubeTitleEn'])
import os, re



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your secret key'
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
    
    @app.route('/dashboardlist', methods=('GET','POST'))
    def dashboardpage(cubelist=cubelist):
        if request.method == 'POST':
            searchterm = request.form['searchfield']
            # if not searchterm:
            #     flash('A search term is required.')
            # else:
            newlist = {}
            reobj = re.compile(searchterm)
            for key in cubelist.keys():
                if(reobj.search(key)):
                    newlist[key] = newlist[key].values
            return redirect("about.html", cubelist=newlist)
        return render_template(
        "dashboardlist.html",
        cubelist=cubelist
    )
    
    @app.route('/about')
    def aboutpage():
        return render_template(
        "about.html"
    )
    
    return app