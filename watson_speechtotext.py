import requests
import json

sample = open('C:/Users/Nivi/Downloads/sample.wav', "rb")

response = requests.post("https://stream.watsonplatform.net/speech-to-text/api/v1/recognize",
         auth = ("73f251fa-f5f6-4270-a4a6-6fdc493610e5", "7aNS7YVLZmaD"),
         headers = {"content-type": "audio/wav"},
         data = sample
         )
 
value = json.loads(response.text)
if value["results"][0]["final"]:
    print (value["results"][0]["alternatives"][0]["transcript"])
    with open("json-output.txt", "w") as text_file:
        print (value["results"][0]["alternatives"][0]["transcript"], file=text_file)
else:
    print ("error in program")
    
