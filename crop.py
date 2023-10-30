import os
import re
import cv2
import argparse
import numpy as np
from PIL import Image
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# mediapipe
model_path = 'models/efficientdet_lite0.tflite'

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.ObjectDetectorOptions(base_options=base_options, score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('directory')
args = parser.parse_args()

# object detection
for file in os.listdir(args.directory):
    image = mp.Image.create_from_file(args.directory + '/' + file)
    detection_result = detector.detect(image)
    results = re.findall("((?:\d\d\d)|(?:\d\d))", str(detection_result)) # sort results
    # crop image
    im = Image.open(args.directory + '/' + file)
    left = int(results[0])
    upper = int(results[1])
    right = int(results[0]) + int(results[2])
    lower = int(results[1]) + int(results[3])
    im1 = im.crop((left, upper, right, lower))
    im1.save(args.directory + '/' + file)



