
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
  
@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"
  
 
@app.route('/duplicate/<int:my_number>')
def duplicate_number(my_number):
    return f'2 x {my_number} = {my_number * 2}'
