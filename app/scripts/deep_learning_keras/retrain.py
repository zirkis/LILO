# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from keras.optimizers import SGD
from keras.utils import np_utils
from imutils import paths
from scipy import sparse
import numpy as np
import argparse
import cv2
import os

from deep_learning_keras.cnn.networks import LeNet, Simple

IMAGE_SIZE = (64, 64)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-s", "--save-model", type=int, default=-1,
	help="(optional) whether or not model should be saved to disk")
ap.add_argument("-l", "--load-model", type=int, default=-1,
	help="(optional) whether or not pre-trained model should be loaded")
ap.add_argument("-w", "--weights", type=str,
	help="(optional) path to weights file")
args = vars(ap.parse_args())



def image_to_feature_vector(image, size=IMAGE_SIZE):
	# resize the image to a fixed size, then flatten the image into
	# a list of raw pixel intensities
	return np.array(cv2.resize(image, size).flatten()) / 255.0

def get_label_from_path(path):
	return os.path.dirname(path).split('/')[-1]

def get_data(dataset_path):
	data = []
	labels = []
	# grab the list of images that we'll be describing
	data_paths = list(paths.list_images(dataset_path))
	for (i, image_path) in enumerate(data_paths):
		data.append(image_path)
		labels.append(get_label_from_path(image_path))
	return (data, labels)

def generator_data(data_path, data_labels):
	while True:
		for (i, image_path) in enumerate(data_path):
			image = cv2.imread(image_path)

			# If the image is corrupted ignore and pass to the next one
			if image is None:
				print("Image: {} is corrupted please move it from the dataset".format(image_path))
				continue

			data = image_to_feature_vector(image)
			data = data.reshape((1, data.shape[0]))
			label = np.array(labels[i]).reshape((1, labels[i].shape[0]))
			yield data, label


(data, labels) = get_data(args["dataset"])
number_of_classes = len(list(set(labels)))

# encode the labels, converting them from strings to integers
le = LabelEncoder()
labels = le.fit_transform(labels)
labels = np_utils.to_categorical(labels, number_of_classes)

# Split the data into two in order to find the accuracy after the training
(train_data, test_data, train_labels, test_labels) = train_test_split(
	data, labels, test_size=0.25, random_state=42)

# initialize the optimizer and model
print("[INFO] compiling model...")
opt = SGD(lr=0.01)

"""
model = LeNet.build(width=IMAGE_SIZE[0], height=IMAGE_SIZE[1], depth=3,
	classes=number_of_classes,
	weightsPath=args["weights"] if args["load_model"] > 0 else None)
"""

model = Simple.build(width=IMAGE_SIZE[0], height=IMAGE_SIZE[1],
	classes=number_of_classes,
	weightsPath=args["weights"] if args["load_model"] > 0 else None)

model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# only train and evaluate the model if we *are not* loading a
# pre-existing model
if args["load_model"] < 0:
	print("[INFO] training...")
	model.fit_generator(generator_data(train_data, train_labels),
		samples_per_epoch = len(train_data),
		nb_epoch = 20)

	# show the accuracy on the testing set
	print("[INFO] evaluating...")
	(loss, accuracy) = model.evaluate_generator(generator_data(test_data, test_labels),
		val_samples=len(test_data))
	print("[INFO] accuracy: {:.2f}%".format(accuracy * 100))

# check to see if the model should be saved to file
if args["save_model"] > 0:
	print("[INFO] dumping weights to file...")
	model.save_weights(args["weights"], overwrite=True)
