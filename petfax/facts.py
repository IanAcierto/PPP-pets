from flask import Flask, Blueprint, render_template, request, redirect
import json
#define json for facts
bp = Blueprint('facts', __name__, url_prefix = '/facts')

@bp.route('/')
def show():
  return render_template('facts.html') #show facts route

@bp.route('/new', methods=['POST', 'GET'])
def new():
  if request.method == 'GET':
    return render_template('new.html')
  if request.method == 'POST':
    print(request.form)
    return redirect('/facts')
    