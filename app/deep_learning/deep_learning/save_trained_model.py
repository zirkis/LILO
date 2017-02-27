# -*- coding: utf-8 -*-

import os
import numpy as np

def save_trained_model(path_to_save, model, labels_name, configs):
	if not os.path.exists(path_to_save):
	    os.makedirs(path_to_save)

	model_json = model.to_json()
	with open("{}/model.json".format(path_to_save), "w") as json_file:
	    json_file.write(model_json)

	model.save_weights("{}/weights.h5".format(path_to_save), overwrite=True)

	np.save("{}/labels.npy".format(path_to_save), labels_name)
	
	np.save('{}/configs.npy', configs) 