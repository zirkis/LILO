# -*- coding: utf-8 -*-

import os
from os import *
from PIL import Image

def create_if_not_exist_dataset_folder(self):
  """
    Create the dataset folder if not exist
  """
  if not os.path.exists(self.path_dataset):
    os.makedirs(self.path_dataset)

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

def insert_in_dataset(label, path_to_add, path_dataset):
	pass
