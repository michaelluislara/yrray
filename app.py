import os

from flask import Flask, render_template


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
        "dashboardlist.html"
    )
    
    @app.route('/about')
    def aboutpage():
        return render_template(
        "about.html"
    )
    
    return app