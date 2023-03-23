from flask import Flask, render_template, request, url_for, redirect, flash, session
import crud
from image_gen import create_custom_image
from model import connect_to_db, db

app = Flask(__name__)
app.secret_key = 'ai_overlords'

@app.route('/')
def homepage():
  # if 'user' in session:
  #   return render_template('homepage.html')
  # else:
  #   return render_template('register_login.html')
  return render_template('register_login.html')

@app.route('/register', methods=['POST'])
def register():
  username = request.form.get('username')
  email = request.form.get('email')
  password = request.form.get('password')
  confirm_password = request.form.get('confirm_password')
  print(username)
  user = crud.get_user_by_email(email)

  if user:
    flash('cannot create an account with that email. Try again')
  elif password != confirm_password:
    flash('your passwords do not match. Try again')
  else:
    user = crud.create_user(username, email, password)
    db.session.add(user)
    db.session.commit()
    flash('Account created! Please log in')
    session['user'] = user
  return redirect('/')

@app.route('/login', methods=['POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')
  user = crud.get_user_by_email(email)

  if not user:
    flash('that user does not exist. Please Register')
  else:
    session['user'] = user
    print(session['user'])

  return redirect('/')

# @app.route('/create_image', methods=['POST'])
# def create_image():
#   prompt_input = request.form['prompt']
#   image_url = create_custom_image(prompt_input)
#   return redirect(url_for('homepage'))

if __name__ == '__main__':
  connect_to_db(app)
  app.run(debug = True, port = 4321, host = 'localhost')