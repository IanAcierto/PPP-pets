from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#flask migrate isn't recognized, can't find it in the bin files.
def create_app():
  app = Flask(__name__)
  app.config['SQLAlchemy_DATABASE_URI'] = 'postgresql://Postgres:643304Ia@localhost:5432/petfax'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  @app.route('/')#assume get method
  def hello():
    return render_template('index.html')
  
  from . import pet, facts, models
  migrate = Migrate(app, models.db)
  models.db.init_app(app)
  app.register_blueprint(pet.bp)
  app.register_blueprint(facts.bp)
  return app