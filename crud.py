from model import db, User

def create_user(username, email, password):
  user = User(username=username, email = email, password=password)
  return user

def get_user_by_id(user_id):
  return User.query.get(user_id)

def get_user_by_email(email):
  return User.query.filter(User.email == email).first()

def get_user_by_username(username):
  return User.query.filter(user.username == username).first()

def log_out(user_id):
  pass

if __name__ == '__main__':
  from server import app
  connect_to_db(app)