from model import db, connect_to_db, User, Story, Scene, Storyboard, Image
from image_gen import create_custom_image

def create_user(username, email, password):
  user = User(username=username, email = email, password=password)
  return user

def get_user_by_email(email):
  return User.query.filter(User.email == email).first()

def create_story(user_id, story_name):
  story = Story(user_id=user_id, story_name=story_name)
  return story

def get_story_by_id(story_id):
  return Story.query.get(story_id)

def create_scene(story_id, scene_description):
  story = Scene(story_id=story_id, scene_description=scene_description)
  return story

def get_scene_by_id(scene_id):
  return Scene.query.get(scene_id)

def create_storyboard(scene_id, storyboard_description, is_favorite):
  storyboard = Storyboard(scene_id=scene_id, storyboard_description=storyboard_description, is_favorite=is_favorite)
  return storyboard

def get_storyboard_by_id(storyboard_id):
  return Storyboard.query.get(storyboard_id)

def create_image(storyboard_id, prompt, url, description):
  image = Image(storyboard_id=storyboard_id, prompt=prompt, url=url, description=description)
  return image

def get_image_by_id(image_id):
  return Image.query.get(image_id)

def update_image_description(image_id, new_description):
  image = Image.query.get(image_id)
  image.description = new_description
  db.session.add(image)
  db.session.commit()

def update_image_prompt(image_id, new_prompt):
  image = Image.query.get(image_id)
  image.prompt = new_prompt
  image.url = create_custom_image(new_prompt)
  db.session.add(image)
  db.session.commit()

if __name__ == '__main__':
  from server import app
  connect_to_db(app)