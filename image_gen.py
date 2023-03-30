import openai
import os

openai.api_key = os.environ['API_KEY']
openai.Model.list()

def create_custom_image(user_prompt):
  response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size='256x256'
  )
  url = response['data'][0]['url']
  return url