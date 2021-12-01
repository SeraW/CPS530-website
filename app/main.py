from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')