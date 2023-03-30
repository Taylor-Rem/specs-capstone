from flask import Flask, render_template, request, url_for, redirect, flash, session

import crud
from model import connect_to_db, db, User

app = Flask(__name__)
app.secret_key = 'ai_overlords'

@app.route('/')
def homepage():
  user = User.query.first()
  if user is not None:
    if 'email' in session:
      email = session['email']
      user = crud.get_user_by_email(email)
      return render_template('homepage.html', user=user)
    else:
      return render_template('register_login.html')
  else:
    return render_template('register_login.html')

@app.route('/register', methods=['POST'])
def register():
  username = request.form.get('username')
  email = request.form.get('email')
  password = request.form.get('password')
  confirm_password = request.form.get('confirm_password')
  user = crud.get_user_by_email(email)

  if user:
    flash('cannot create an account with that email. Try again')
  elif password != confirm_password:
    flash('your passwords do not match. Try again')
  else:
    user = crud.create_user(username, email, password)
    db.session.add(user)
    db.session.commit()

    session['email'] = email
  return redirect('/')

@app.route('/login', methods=['POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')
  user = crud.get_user_by_email(email)

  if not user:
    flash('that user does not exist. Please Register')
  else:
    session['email'] = email
  return redirect('/')

@app.route('/logout')
def logout():
  del session['email']
  flash('logged out')
  return redirect ('/')

@app.route('/user/<int:user_id>')
def user(user_id):
  user = crud.get_user_by_email(session['email'])
  return render_template('user_details.html', user=user)

@app.route('/add_story', methods=['POST'])
def add_story():
  user = crud.get_user_by_email(session['email'])
  user_id = user.user_id
  story_name = request.form.get('story_name')
  story = crud.create_story(user_id, story_name)
  db.session.add(story)
  db.session.commit()
  return redirect('/')

@app.route('/open_story/<int:story_id>')
def open_story(story_id):
  user = crud.get_user_by_email(session['email'])
  story = crud.get_story_by_id(story_id)
  return render_template('story_details.html', user=user, story=story)

@app.route('/add_scene', methods=['POST'])
def add_scene():
  user = crud.get_user_by_email(session['email'])
  scene_name = request.form.get('scene_name')
  story_id = request.form.get('story_id')
  scene = crud.create_scene(story_id, scene_name)
  db.session.add(scene)
  db.session.commit()
  return redirect(f'/open_story/{story_id}')

@app.route('/open_scene/<int:scene_id>')
def open_scene(scene_id):
  user = crud.get_user_by_email(session['email'])
  scene = crud.get_scene_by_id(scene_id)
  return render_template('scene_details.html', user=user, scene=scene)

@app.route('/add_storyboard', methods=['POST'])
def add_storyboard():
  user = crud.get_user_by_email(session['email'])
  scene_id = request.form.get('scene_id')
  storyboard_description = request.form.get('storyboard_description')
  is_favorite = False
  storyboard = crud.create_storyboard(scene_id, storyboard_description, is_favorite)
  db.session.add(storyboard)
  db.session.commit()
  return redirect(f'/open_scene/{scene_id}')

@app.route('/open_storyboard/<int:storyboard_id>')
def open_storyboard(storyboard_id):
  user = crud.get_user_by_email(session['email'])
  storyboard = crud.get_storyboard_by_id(storyboard_id)
  return render_template('storyboard_details.html', user=user, storyboard=storyboard)

@app.route('/create_image', methods=['POST'])
def create_image():
  storyboard_id = request.form['storyboard_id']
  prompt = request.form['prompt']
  description = request.form['description']
  url = request.form['url']
  image = crud.create_image(storyboard_id, prompt, url, description)
  db.session.add(image)
  db.session.commit()
  return redirect(f'/open_storyboard/{storyboard_id}')

if __name__ == '__main__':
  connect_to_db(app)
  app.run(debug = True, port = 4321, host = 'localhost')