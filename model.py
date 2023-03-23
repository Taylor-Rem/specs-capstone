from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  username = db.Column(db.String, unique=True)
  email = db.Column(db.String, unique=True)
  password = db.Column(db.String)

  def __repr__(self):
    return f"<User user_id={self.user_id} email={self.email} username={self.username}>"
  
class Story(db.Model):
  __tablename__ = 'stories'

  story_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  story_name = db.Column(db.String)

class Scene(db.Model):
  __tablename__ = 'scenes'

  scene_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  story_id = db.Column(db.Integer, db.ForeignKey('stories.story_id'))
  scene_description = db.Column(db.String)

class Storyboard(db.Model):
  __tablename__ = 'storyboards'

  storyboard_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  scene_id = db.Column(db.Integer, db.ForeignKey('scenes.scene_id'))
  storyboard_description = db.Column(db.String)
  is_favorite = db.Column(db.Boolean, unique=True, default=False)

class Image(db.Model):
  __tablename__ = 'images'

  image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  storyboard_id = db.Column(db.Integer, db.ForeignKey('storyboards.storyboard_id'))
  prompt = db.Column(db.String)
  url = db.Column(db.String)
  description = db.Column(db.String)

def connect_to_db(flask_app, echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['POSTGRES_URI']
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == '__main__':
  from server import app
  connect_to_db(app)