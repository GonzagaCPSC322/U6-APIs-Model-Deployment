import requests # lib to make http requests
import json # lib to help with parsing JSON objects

url = "https://itunes.apple.com/search?term=thor&media=movie"

# make a GET request to get the search results back
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
response = requests.get(url=url)

# first thing... check the response status code 
status_code = response.status_code
print("status code:", status_code)

if status_code == 200:
    # success! grab the message body
    json_object = json.loads(response.text)
    #print(json_object)
    results_array = json_object["results"]
    for result in results_array:
        #print("result:", result, "\n")
        # task: print out the name and its duration (run time) in hours
        name = result["trackName"]
        duration = result["trackTimeMillis"]
        print(name, ":", duration)