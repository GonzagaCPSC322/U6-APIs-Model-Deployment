import requests # lib for making requests
import json # lib for parsing strings/JSON objects

url = "https://itunes.apple.com/search?term=thor&media=movie"

# make the GET request
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
response = requests.get(url=url)

# first, check the status code!!
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
status_code = response.status_code
print("status_code:", status_code)

if status_code == 200:
    # success! can grab message body 
    json_object = json.loads(response.text)
    print(json_object)
    results_array = json_object["results"]
    for result in results_array:
        print("result:", result, "\n")
        # task: print out the name and run time (duration) in hours
