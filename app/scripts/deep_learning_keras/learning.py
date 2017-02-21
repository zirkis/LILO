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

IMAGE_SIZE = (32, 32)
CLASSES = 3

def image_to_feature_vector(image, size=IMAGE_SIZE):
	# resize the image to a fixed size, then flatten the image into
	# a list of raw pixel intensities
	return cv2.resize(image, size).flatten()

def get_label_from_path(path):
	return os.path.dirname(path).split('/')[-1]

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

 
# grab the list of images that we'll be describing
print("[INFO] describing images...")
imagePaths = list(paths.list_images(args["dataset"]))
 
# initialize the data matrix and labels list
data = []
labels = []

# loop over the input images
for (i, imagePath) in enumerate(imagePaths):
	# load the image and extract the class label (assuming that our
	# path as the format: /path/to/dataset/{class}/{imageName}.jpg
	image = cv2.imread(imagePath)
	label = get_label_from_path(imagePath)

	# If the image is corrupted ignore and pass to the next one
	if image is None:
		continue

	# construct a feature vector raw pixel intensities, then update
	# the data matrix and labels list
	features = image_to_feature_vector(image)
	data.append(features)
	labels.append(label)
 
	# show an update every 1,000 images
	if i > 0 and i % 1000 == 0:
		print("[INFO] processed {}/{}".format(i, len(imagePaths)))

# encode the labels, converting them from strings to integers
le = LabelEncoder()
labels = le.fit_transform(labels)

# scale the input image pixels to the range [0, 1], then transform
# the labels into vectors in the range [0, num_classes] -- this
# generates a vector for each label where the index of the label
# is set to `1` and all other entries to `0`
data = np.array(data) / 255.0

labels = np_utils.to_categorical(labels, CLASSES)

# partition the data into training and testing splits, using 75%
# of the data for training and the remaining 25% for testing
print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(
	data, labels, test_size=0.25, random_state=42)

# initialize the optimizer and model
print("[INFO] compiling model...")
opt = SGD(lr=0.01)


"""
model = LeNet.build(width=IMAGE_SIZE[0], height=IMAGE_SIZE[1], depth=3,
	classes=CLASSES,
	weightsPath=args["weights"] if args["load_model"] > 0 else None)
"""

model = Simple.build(width=IMAGE_SIZE[0], height=IMAGE_SIZE[1],
	classes=CLASSES,
	weightsPath=args["weights"] if args["load_model"] > 0 else None)

model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["accuracy"])

print(testLabels[0])
# only train and evaluate the model if we *are not* loading a
# pre-existing model
if args["load_model"] < 0:
	print("[INFO] training...")
	model.fit(trainData, trainLabels, batch_size=128, nb_epoch=20,
		verbose=1)
	# show the accuracy on the testing set
	print("[INFO] evaluating...")
	(loss, accuracy) = model.evaluate(testData, testLabels,
		batch_size=128, verbose=1)
	print("[INFO] accuracy: {:.2f}%".format(accuracy * 100))

# check to see if the model should be saved to file
if args["save_model"] > 0:
	print("[INFO] dumping weights to file...")
	model.save_weights(args["weights"], overwrite=True)
