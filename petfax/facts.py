from flask import Flask, Blueprint, render_template
import json
#define json for facts
bp = Blueprint('facts', __name__, url_prefix = '/facts')

@bp.route('/')
def show():
  pass #show facts route

@bp.route('/new')
def new():
  return render_template('new.html')