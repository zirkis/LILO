# -*- coding: utf-8 -*-

import os
from imutils import paths

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