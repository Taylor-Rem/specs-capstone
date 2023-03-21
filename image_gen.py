import openai

openai.api_key = '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'
openai.Model.list()

def create_custom_image(user_prompt):
  response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size='256x256'
  )
  url = response['data'][0]['url']
  return url