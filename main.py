from flask import Flask
from website import create_app

app = create_app()
#app = Flask(__name__)

#@app.route('/')
#def index():
#return 'Hello from Flask!'

if __name__ == '__main__':
  app.run(debug=True)
  #app.run(host='0.0.0.0', port=81)
