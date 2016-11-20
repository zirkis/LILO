# -*- coding: utf-8 -*-

import os
from os import *
from PIL import Image
from icrawler.examples import GoogleImageCrawler

class PicturesManager:

	def __init__(self, pathPictures):
		self.pathPictures = pathPictures

	def downloadPictures(self, search, numberOfPictures, pathToSave=None):
		if pathToSave is None:
			pathToSave = self.pathPictures
		googleCrawler = GoogleImageCrawler(path_to_save=pathToSave, img_dir=search)
		googleCrawler.crawl(keyword=search, offset=0, max_num=numberOfPictures,
			date_min=None, date_max=None, feeder_thr_num=1,
			parser_thr_num=1, downloader_thr_num=4,
			min_size=(200,200), max_size=None)

	def convertPicturesToFormat(self, folderPath=None, picturesFormat='jpg', deletePictureIfError= True):
		if self._hasCorrectFormat(picturesFormat) is False:
			return False

		if folderPath is None:
			folderPath = self.pathPictures

		for (path, dirs, files) in os.walk(folderPath):
			for file in files:
				success = self.convertPictureToFormat(path + '/' + file, picturesFormat)
				if success is not True and deletePictureIfError:
					print('Delete: ' + path + '/' + file)
					remove(path + '/' + file)
		return True

	def convertPictureToFormat(self, picturePath, format='jpg'):
		infoPicture = self.getInfosPicture(picturePath)

		if infoPicture is not None:
			if infoPicture['format'] == format:
				return True
			try:
				im = Image.open(infoPicture['dirname'] + '/' + infoPicture['name'] + '.' + infoPicture['format']).convert('RGB')
				im.save(infoPicture['dirname'] + '/' + infoPicture['name'] + '.' + format)
				remove(infoPicture['dirname'] + '/' + infoPicture['name'] + '.' + infoPicture['format'])
				return True
			except IOError:
				print('Error with: ' + infoPicture['dirname'] + '/' + infoPicture['name'] + '.' + infoPicture['format'])
				pass
		return False

	def getInfosPicture(self, picturePath):
		basename = path.basename(picturePath)
		pictureFormat = path.splitext(basename)[1][1:]
		if self._hasCorrectFormat(pictureFormat) is False:
			return None
		dirname =path.dirname(picturePath)
		name = path.splitext(basename)[0]

		return {'dirname': dirname,
						'name': name,
						'format': pictureFormat
						}

	def _hasCorrectFormat(self, pictureFormat):
		pictureFormat = pictureFormat.upper()
		if (pictureFormat == 'BMP' or 
					pictureFormat == 'JPEG' or
					pictureFormat == 'JPG' or
					pictureFormat == 'PNG'):
				return True;
		return False

