# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense

class LeNet:
	"""
	Params:
		width       : The width of our input images.
		height      : The height of our input images.
		depth       : The depth (i.e., number of channels) of our input images.
		classes     : And the number of classes (i.e., unique number of class labels) in our dataset.
		weightsPath : Can be used to load a pre-trained model
	"""
	@staticmethod
	def build(width, height, depth, classes, weightsPath=None):
		model                 = Sequential()
		convolution_filter    = 20
		filter_size           = (5, 5)
		fully_connected_layer = 500

		# first set of CONV => RELU => POOL
		model.add(Convolution2D(convolution_filter, filter_size[0],
			filter_size[1], border_mode="same",
			input_shape=(height, width, depth)))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

		convolution_filter = 50

		# second set of CONV => RELU => POOL
		model.add(Convolution2D(convolution_filter, filter_size[0],
			filter_size[1], border_mode="same",
			input_shape=(height, width, depth)))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

		# set of FC => RELU layers
		model.add(Flatten())
		model.add(Dense(fully_connected_layer))
		model.add(Activation("relu"))
 
		# softmax classifier
		model.add(Dense(classes))
		model.add(Activation("softmax"))

		# if a weights path is supplied (inicating that the model was
		# pre-trained), then load the weights
		if weightsPath is not None:
			model.load_weights(weightsPath)
 
		# return the constructed network architecture
		return model