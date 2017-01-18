# -*- coding: utf-8 -*-

import os
from os import *
from PIL import Image
from icrawler.examples import GoogleImageCrawler

class PicturesManager:

	def __init__(self, path_pictures):
		self.path_pictures = path_pictures

	def download_pictures(self, search, number_of_results, path_to_save=None):
		if path_to_save is None:
			path_to_save = self.pathPictures
		google_crawler = GoogleImageCrawler(path_to_save, search)
		google_crawler.crawl(
			keyword=search,
			offset=0,
			max_num=number_of_results,
			date_min=None,
			date_max=None,
			feeder_thr_num=1,
			parser_thr_num=1,
			downloader_thr_num=4,
			min_size=(200,200),
			max_size=None)

	def convert_pictures_to_format(self, 
		folder_path=None,
		pictures_format='jpg',
		delete_picture_if_error=True):

		print("Convert pictures to {}".format(pictures_format))
		if self._has_correct_format(pictures_format) is False:
			return False

		if folder_path is None:
			folder_path = self.path_pictures

		is_root_dir = True
		for (path, dirs, files) in os.walk(folder_path):
			if is_root_dir:
				is_root_dir = False
				continue
			print("Move to : {}".format(path))
			for file in files:
				success = self.convert_picture_to_format(path + '/' + file, pictures_format)
				if success is not True and delete_picture_if_error:
					print('Delete: ' + path + '/' + file)
					remove(path + '/' + file)
		return True

	def convert_picture_to_format(self, picture_path, picture_format='jpg'):
		info_picture = self.get_infos_picture(picture_path)

		if info_picture is not None:
			try:
				im = Image.open(info_picture['dirname'] + '/' + info_picture['name'] + '.' + info_picture['format']).convert('RGB')
				im.save(info_picture['dirname'] + '/' + info_picture['name'] + '.' + picture_format)
				if info_picture['format'] != picture_format:
					remove(info_picture['dirname'] + '/' + info_picture['name'] + '.' + info_picture['format'])
				return True
			except IOError:
				print('Corrupt file: ' + info_picture['dirname'] + '/' + info_picture['name'] + '.' + info_picture['format'])
				pass
		return False

	def get_infos_picture(self, picture_path):
		basename = path.basename(picture_path)
		picture_format = path.splitext(basename)[1][1:]
		if self._has_correct_format(picture_format) is False:
			return None
		dirname =path.dirname(picture_path)
		name = path.splitext(basename)[0]

		return {'dirname': dirname,
						'name': name,
						'format': picture_format
						}

	def _has_correct_format(self, picture_format):
		picture_format = picture_format.upper()
		if (picture_format == 'BMP' or 
					picture_format == 'JPEG' or
					picture_format == 'JPG' or
					picture_format == 'PNG'):
				return True;
		return False
