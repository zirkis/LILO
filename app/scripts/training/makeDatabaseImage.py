# -*- coding: utf-8 -*-

from utils.pictures_manager import PicturesManager

if __name__ == '__main__':

	pathToSave = "../../data"

	pictureManager = PicturesManager(pathToSave)

	searchies = ["plane", "car", "house"]
	numberOfPictures = 10

	for search in searchies:
		pictureManager.downloadPictures(search, numberOfPictures)

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
