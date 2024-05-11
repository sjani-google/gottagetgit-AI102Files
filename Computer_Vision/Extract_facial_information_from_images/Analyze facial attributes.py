import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os
import json


# def config():
#     print("Call Config")
#     return subscription_key, face_api_url

face_api_url = "https://cdn.profoto.com/cdn/053149e/contentassets/d39349344d004f9b8963df1551f24bf4/profoto-albert-watson-steve-jobs-pinned-image-original.jpg?width=1280&quality=75&format=jpg"
image_path = os.path.join(r'CapFrame.jpg')
print(image_path)
image_data = open(image_path, "rb")

endpoint = os.environ["FACEAPI_ENDPOINT"]
subscription_key = os.environ["FACEAPI_KEY"]

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}

response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
faces = response.json()
print(faces)
with open("faces.json", "w") as faces_file:
    json.dump(faces, faces_file, indent=4, sort_keys=True)
