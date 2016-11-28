# -*- coding: utf-8 -*-

from pictures_manager import PicturesManager

if __name__ == '__main__':
	print("Initialisation du script\n")
	

	pathToSave = "../makeDB"
	pictureManager = PicturesManager(pathToSave)
	"""
	pictureManager = PicturesManager(pathToSave)

	aromaticsSearch = ["Basil leaf",
									 "Parsley leaf",
									 "Mint leaf",
									 "Thyme leaf",
									 "Thai basil leaf",
									 "Purple basil leaf"]

	flowersSearch = ["Sunflower",
									"Purslane",
									"Petunia"]

	fruitsAndVegetables = ["lettuce",
												"cherry",
												"tomato",
												"pepper mini"]

	searches = aromaticsSearch + flowersSearch + fruitsAndVegetables

	numberOfPictures = 1000

	for search in searches:
		pictureManager.downloadPictures(search, numberOfPictures)						 
	"""
	numberOfPictures = 1000
	search = "lettuce"
	pictureManager.downloadPictures(search, numberOfPictures)		
	pictureManager.convertPicturesToFormat()


	print("Fin du script\n")


"""
	python retrain.py \
--bottleneck_dir=../train_data/bottlenecks \
--how_many_training_steps 500 \
--model_dir=../train_data/inception \
--output_graph=../train_data/retrained_graph.pb \
--output_labels=../train_data/retrained_labels.txt \
--image_dir ../plants
"""