import os
AZURE_API_KEY = os.getenv('AZURE_API_KEY')

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person


subscription_key = os.getenv('AZURE_VISION_API_KEY')
endpoint = os.getenv('AZURE_VISION_API_ENDPOINT')

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
local_image_handwritten_path = "/Users/tim/Pictures/driverslicense2.jpg"
local_image_handwritten = open(local_image_handwritten_path, "rb")

# Call API with image and raw response (allows you to get the operation location)
read_results = computervision_client.read_in_stream(local_image_handwritten, raw=True)
# Get the operation location (URL with ID as last appendage)
operation_location_local = read_results.headers["Operation-Location"]
# Take the ID off and use to get results
operation_id_local = operation_location_local.split("/")[-1]

# Call the "GET" API and wait for the retrieval of the results
while True:
    read_result = computervision_client.get_read_result(operation_id_local)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print results, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)
print()

subscription_key = os.getenv('AZURE_FACE_API_KEY')
endpoint = os.getenv('AZURE_FACE_API_ENDPOINT')
face_client = FaceClient(endpoint, CognitiveServicesCredentials(subscription_key))
print(face_client.face.detect_with_stream(open('/Users/tim/Pictures/meinbathroom.jpg', 'rb'), detectionModel='detection_02'))
print(face_client.face.detect_with_stream(open('/Users/tim/Pictures/driverslicense2.jpg', 'rb'), detectionModel='detection_02'))

image1 = face_client.face.detect_with_stream(open('/Users/tim/Pictures/meinbathroom.jpg', 'rb'), detectionModel='detection_02')[0].face_id
image2 = face_client.face.detect_with_stream(open('/Users/tim/Pictures/driverslicense2.jpg', 'rb'), detectionModel='detection_02')[0].face_id
# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    
    return ((left, top), (right, bottom))


img = Image.open(open('/Users/tim/Pictures/meinbathroom.jpg', 'rb'))

# For each face returned use the face rectangle and draw a red box.
print('Drawing rectangle around face... see popup for results.')
draw = ImageDraw.Draw(img)
draw.rectangle(getRectangle(face_client.face.detect_with_stream(open('/Users/tim/Pictures/meinbathroom.jpg', 'rb'), detectionModel='detection_02')[0]), outline='red')

# Display the image in the users default image browser.
#img.show()
img = Image.open(open('/Users/tim/Pictures/driverslicense.jpg', 'rb'))

# For each face returned use the face rectangle and draw a red box.
print('Drawing rectangle around face... see popup for results.')
draw = ImageDraw.Draw(img)
draw.rectangle(getRectangle(face_client.face.detect_with_stream(open('/Users/tim/Pictures/driverslicense.jpg', 'rb'), detectionModel='detection_02')[0]), outline='red')

# Display the image in the users default image browser.
img.show()
verify_result_same = face_client.face.verify_face_to_face(image1, image2)
print('the same person, with confidence: {}'
    .format(verify_result_same.confidence)
    if verify_result_same.is_identical
    else 'different person, with confidence: {}'
        .format(verify_result_same.confidence))