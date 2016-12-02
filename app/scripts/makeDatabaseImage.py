# -*- coding: utf-8 -*-

from pictures_manager import PicturesManager

if __name__ == '__main__':

	pathToSave = "../data"

	pictureManager = PicturesManager(pathToSave)

	searchs = ["plane", "car", "house"]
	numberOfPictures = 1000

	pictureManager.downloadPictures(searchs, numberOfPictures)		
	pictureManager.convertPicturesToFormat()





	"""

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