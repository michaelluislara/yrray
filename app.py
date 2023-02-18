import requests
from flask import Flask, render_template, request, url_for, flash, redirect
from forms import LoginForm, SearchForm
from config import Config
cubes = requests.get('https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesListLite', stream=True)
cubelist = cubes.json()
cubelist = sorted(cubelist, key=lambda d: d['cubeTitleEn'])
import os, re, models
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import markupsafe



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)
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
        form = SearchForm()
        if form.validate_on_submit():
            newlist = []
            reobj = re.compile(markupsafe.escape(form.searchterm.data), re.IGNORECASE)
            for i in cubelist:
                result = reobj.search(string=i['cubeTitleEn'])
                if result is not None:
                    newlist.append(i)
            return render_template("dashboardlist.html", cubelist=newlist, form=form)
            
            # return redirect('/about')
        return render_template(
        "dashboardlist.html",
        cubelist=cubelist, form=form)
    
    @app.route('/about')
    def aboutpage():
        return render_template(
        "about.html"
    )
        
    @app.route('/login', methods=('GET','POST'))
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
            return redirect('/about')
        return render_template("login.html", title='Sign In', form=form)
    
    return app