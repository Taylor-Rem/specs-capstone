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
    return f"<User user_id={self.user_id} email={self.email}>"
  
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