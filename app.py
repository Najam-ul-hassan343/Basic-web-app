from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome_message():
 return 'Hello,Najam! You have successfully Deployed the application'

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)

