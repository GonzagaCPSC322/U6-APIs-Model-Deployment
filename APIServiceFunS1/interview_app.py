# we are going to use a micro web framework called Flask
# to create our web app (for running an API service)

from flask import Flask

# by default flask runs on port 5000

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)