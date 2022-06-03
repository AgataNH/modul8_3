from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"

from flask import render_template
from flask import request
from flask import redirect

@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")