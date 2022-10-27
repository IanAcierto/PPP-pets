"""from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
  return 'hit the home route!'"""
  
from petfax import create_app
app = create_app