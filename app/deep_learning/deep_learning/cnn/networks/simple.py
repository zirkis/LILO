# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense

class Simple:
	"""
	Params:
		width       : The width of our input images.
		height      : The height of our input images.
		classes     : And the number of classes (i.e., unique number of class labels) in our dataset.
		weightsPath : Can be used to load a pre-trained model
	"""
	@staticmethod
	def build(width, height, classes, weightsPath=None):
		model = Sequential()

		model = Sequential()
		model.add(Flatten(input_shape=(width, height, 3)))
		model.add(Dense(768, input_dim=(width * height * 3),
			init="uniform", activation="relu"))
		model.add(Dense(384, init="uniform", activation="relu"))
		model.add(Dense(classes))
		model.add(Activation("softmax"))

		# if a weights path is supplied (inicating that the model was
		# pre-trained), then load the weights
		if weightsPath is not None:
			model.load_weights(weightsPath)
 
		# return the constructed network architecture
		return model