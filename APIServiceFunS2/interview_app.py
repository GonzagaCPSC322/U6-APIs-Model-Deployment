# we are going to use Flask, a micro web framework

from flask import Flask 

# make a Flask app
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True) # TODO: set debug to False for production
    # by default, Flask runs on port 5000
