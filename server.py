from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

from image_gen import create_custom_image

logged_in = False

@app.route('/')
def homepage():
  
  if not logged_in:
    return render_template('register_login.html')

  return render_template('homepage.html')

# @app.route('/create_image', methods=['POST'])
# def create_image():
#   prompt_input = request.form['prompt']
#   image_url = create_custom_image(prompt_input)
#   return redirect(url_for('homepage'))

if __name__ == '__main__':
  app.run(debug = True, port = 4321, host = 'localhost')