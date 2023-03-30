from model import db, connect_to_db, User, Story, Scene, Storyboard, Image

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

if __name__ == '__main__':
  from server import app
  connect_to_db(app)