# -*- coding: utf-8 -*-

import os
import numpy as np

def load_saved_trained_model(path_to_model):
	json_file = open("{}/model.json".format(path_to_model), 'r')
	model_json = json_file.read()
	json_file.close()

	model = model_from_json(model_json)
	model.load_weights("{}/weights.h5".format(path_to_model))

	labels = np.load("{}/labels.npy".format(path_to_model))

	configs = np.load("{}/configs.npy".format(path_to_model))

	return (model, labels, configs)
