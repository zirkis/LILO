# -*- coding: utf-8 -*-

from utils.pictures_manager import PicturesManager

if __name__ == '__main__':

	pathToSave = "../../data"

	pictureManager = PicturesManager(pathToSave)
	
	pictureManager.convertPicturesToFormat()

