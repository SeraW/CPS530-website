from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/form', methods=["POST"])
def form():
    first_name= request.form.get("first_name")
    last_name= request.form.get("last_name")
    email= request.form.get("email")
    age= request.form.get("age")
    cereal= request.form.getlist("cereal")
    dealbreaker= request.form.get("dealbreaker")

    if int(age) > 499:
        return render_template('old.html')
    elif len(cereal) < 4 or dealbreaker == None:
        return render_template('noentry.html')
    else:
        return render_template('form.html', first_name=first_name, last_name=last_name, email=email, age=age,cereal=cereal,dealbreaker=dealbreaker)