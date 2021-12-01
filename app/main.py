from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')