# we are going to use a micro web framework called Flask
# to create our web app (for running an API service)

from flask import Flask, jsonify, request 

# by default flask runs on port 5000

app = Flask(__name__)

# we need to define "routes", functions that 
# handle requests
# let's add a route for the "homepage"
@app.route("/", methods=["GET"])
def index():
    # return content and status code
    return "Welcome to my App!!", 200

# add a route for "/predict" API endpoint
@app.route("/predict", methods=["GET"])
def predict():
    # goal is to parse the query string to the args
    # query args are in the request object
    level = request.args.get("level", "")
    print("level:", level)
    # task: extract the other three parameters
    # level, lang, tweets, phd
    # make a prediction with the tree
    # respond to the client with the prediction in a JSON object
    result = {"prediction": "True"} # TODO: fix hardcoding
    return jsonify(result), 200 

if __name__ == "__main__":
    app.run(debug=True)