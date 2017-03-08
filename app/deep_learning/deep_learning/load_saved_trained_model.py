# -*- coding: utf-8 -*-

import os
import deepdish as dd
from keras.models import model_from_json

def load_saved_trained_model(path_to_model):
	json_file = open("{}/model.json".format(path_to_model), 'r')
	model_json = json_file.read()
	json_file.close()

	model = model_from_json(model_json)
	model.load_weights("{}/weights.h5".format(path_to_model))

	total_configs = dd.io.load("{}/configs.h5".format(path_to_model))
	
	labels = total_configs['labels']
	configs = total_configs['configs']

	return (model, labels, configs)
