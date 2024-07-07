# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
#instance of bootstrap
bootstrap = Bootstrap5(app)
# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '<p>Prayash S.:- LASER</p>'

@app.route('/prayash')
def hello_prayash():
  return render_template('template.html')