# -*- coding: utf-8 -*-

from utils.pictures_manager import PicturesManager

if __name__ == '__main__':

	pathToSave = "../../data"

	pictureManager = PicturesManager(pathToSave)

	searchies = {"plane": "plane", "car": "car", "house": "house"}
	numberOfPictures = 10

	for folderToSave, search in searchies.iteritems():
		pictureManager.downloadPictures(search, numberOfPictures, "../../data/{}".format(folderToSave))

	pictureManager.convertPicturesToFormat()

	"""
	aromaticsSearchies = {"basil": "Basil leaf",
									 "parsley": "Parsley leaf",
									 "mint": "Mint leaf",
									 "thyme": "Thyme leaf",
									 "thai basil": "Thai basil leaf",
									 "purple basil": "Purple basil leaf"}

	flowersSearchies = {"sunflower": "Sunflower",
									"purslane": "Purslane",
									"petunia": "Petunia"}

	fruitsAndVegetablesSearchies = {"lettuce": "lettuce",
												"cherry": "cherry",
												"tomato": "tomato",
												"pepper mini": "pepper mini"}

	searchies = aromaticsSearchies + flowersSearchies + fruitsAndVegetablesSearchies

	numberOfPictures = 1000

	for folderToSave, search in searchies.iteritems():
		pictureManager.downloadPictures(search, numberOfPictures, "../../data/{}".format(folderToSave))					 
	"""
