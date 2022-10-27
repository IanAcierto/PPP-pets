from flask import Flask, render_template

def create_app():
  app = Flask(__name__)
  
  @app.route('/')#assume get method
  def hello():
    return render_template('index.html')
  
  from . import pet, facts
  app.register_blueprint(pet.bp)
  app.register_blueprint(facts.bp)
  return app