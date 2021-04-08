# we are going to use a micro web framework called Flask
# to create our web app (for running an API service)
import os 
import pickle 
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
    lang = request.args.get("lang", "")
    tweets = request.args.get("tweets", "")
    phd = request.args.get("phd", "")
    print("level:", level, lang, tweets, phd)
    # task: extract the other three parameters
    # level, lang, tweets, phd
    # make a prediction with the tree
    # respond to the client with the prediction in a JSON object
    prediction = predict_interviews_well([level, lang, tweets, phd])
    if prediction is not None:
        result = {"prediction": prediction} 
        return jsonify(result), 200 
    else:
        return "Error making prediction", 400

def tdidt_predict(header, tree, instance):
    # returns "True" or "False" if a leaf node is hit
    # None otherwise 
    info_type = tree[0]
    if info_type == "Attribute":
        # get the value of this attribute for the instance
        attribute_index = header.index(tree[1])
        instance_value = instance[attribute_index]
        for i in range(2, len(tree)):
            value_list = tree[i]
            if value_list[1] == instance_value:
                # recurse, we have a match!!
                return tdidt_predict(header, value_list[2], instance)
    else: # Leaf
        return tree[1] # label
    

def predict_interviews_well(instance):
    # I need the tree and its header in order to make a prediction for instance
    # import pickle.... depickle tree.p
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile)
    infile.close()

    print("header:", header)
    print("tree:", tree)

    # traverse the tree to make a prediction
    # write a recursive algorithm to do this (predict() for PA6)
    try:
        return tdidt_predict(header, tree, instance)
    except:
        # something went wrong
        return None 


if __name__ == "__main__":
    # deployment notes
    # two main categories of deployment
    # host your own server OR use a cloud provider
    # quite a few cloud provider options... AWS, Heroku, Azure, DigitalOcean,...
    # we are going to use Heroku (backend as a service BaaS)
    # there are quite a few ways to deploy a Flask app on Heroku
    # 1. deploy the app directly on an ubuntu "stack" (e.g. Procfile and requirements.txt)
    # 2. deploy the app as a Docker container on a container "stack" (e.g. Dockerfile)
    # 2.A. build a Docker image locally and push the image to a container registry 
    # (e.g. Heroku's registry)
    # **2.B.** define a heroku.yml and push our source code to Heroku's git
    # and Heroku is going to build the Docker image (and register it)
    # 2.C. define main.yml and push our source code to Github and Github
    # (via a Github Action) builds the image and pushes the image to Heroku

    # we need to change app settings for deployment
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)