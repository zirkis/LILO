# -*- coding: utf-8 -*-

import os
import uuid
from os import *
from PIL import Image
from shutil import copyfile

def create_if_not_exist_dataset_folder(path_dataset):
  """
    Create the dataset folder if not exist
  """
  if not os.path.exists(path_dataset):
    os.makedirs(path_dataset)

def image_has_correct_format(picture_format):
  picture_format = picture_format.upper()
  if (picture_format == 'BMP' or 
      picture_format == 'JPEG' or
      picture_format == 'JPG' or
      picture_format == 'PNG'):
      return True;
  return False

def get_infos_picture(picture_path):
  basename = path.basename(picture_path)
  picture_format = path.splitext(basename)[1][1:]
  if image_has_correct_format(picture_format) is False:
    return None
  dirname =path.dirname(picture_path)
  name = path.splitext(basename)[0]

  return {'dirname': dirname,
          'name': name,
          'format': picture_format
          }

def convert_picture_to_jpg(picture_path):
  info_picture = get_infos_picture(picture_path)

  if info_picture is not None:
    try:
      im = Image.open(info_picture['dirname'] + '/' + info_picture['name'] + '.' + info_picture['format']).convert('RGB')
      im.save(info_picture['dirname'] + '/' + info_picture['name'] + '.jpg')
      if info_picture['format'] != 'jpg':
        remove(info_picture['dirname'] + '/' + info_picture['name'] + '.' + info_picture['format'])
      return True
    except IOError:
      print('Corrupt file: ' + info_picture['dirname'] + '/' + info_picture['name'] + '.' + info_picture['format'])
  return False

def convert_pictures_to_jpg(folder_path,
    delete_picture_if_error=True):
  pictures_format='jpg'

  print('Begin conversion to {}'.format(pictures_format))
  for (path, dirs, files) in os.walk(folder_path):
    print("Move to : {}".format(path))
    for file in files:
      success = convert_picture_to_jpg(path + '/' + file)
      if success is not True and delete_picture_if_error:
        print('Delete: ' + path + '/' + file)
        remove(path + '/' + file)
  return True

def transfert_image_to_dataset(label, path_to_add, path_dataset):
  path_label = '{}/{}'.format(path_dataset, label)

  if not os.path.exists(path_label):
    os.makedirs(path_label)

  for (path, dirs, files) in os.walk(path_to_add):
    print("Move to : {}".format(path))
    for file in files:
      src = '{}/{}'.format(path, file)
      dst = '{}/{}.jpg'.format(path_label, uuid.uuid4())
      copyfile(src, dst)

def insert_in_dataset(label, path_to_add, path_dataset):
  if not os.path.exists(path_to_add):
    message = 'Path to add doesn\'t exist: {}'.format(path_to_add)
    print(message)
    return

  create_if_not_exist_dataset_folder(path_dataset)
  convert_pictures_to_jpg(path_to_add)
  transfert_image_to_dataset(label, path_to_add, path_dataset)
