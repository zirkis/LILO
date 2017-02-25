# -*- coding: utf-8 -*-

import cv2
import numpy as np
import argparse
from keras.models import model_from_json

IMAGES_SIZE = (64, 64)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
	type=str, help="Path to file to predict")
ap.add_argument("-m", "--model", required=True,
	type=str, help="Path to the folder containing the model and the weights")
args = vars(ap.parse_args())

print("[INFO] Loading model from disk...")
 # load json and create model
json_file = open("{}/model.json".format(args["model"]), 'r')
model_json = json_file.read()
json_file.close()

model = model_from_json(model_json)
model.load_weights("{}/weights.h5".format(args["model"]))

print("[INFO] Loading labels from disk...")
labels = np.load("{}/labels.npy".format(args["model"]))

print("[INFO] Loading given image from disk...")
image = cv2.imread(args["file"])

if image is None:
	print("Error during loading the image")
else:
	image = np.array(cv2.resize(image, IMAGES_SIZE).flatten()) / 255.0
	image = image.reshape((1, image.shape[0]))
	classes = model.predict(image)
	np.set_printoptions(formatter={'float_kind':'{:f}'.format})
	
	print("RESULT:")
	for i in range(0, len(classes[0])):
		print("{}: {}".format(labels[i], classes[0][i] * 100))

# python predict_cnn_example.py -f "image.jpg" -w "output.h5"
