# -*- coding: utf-8 -*-
import os
from os import *
import cv2
from utils.dataset.pictures_manager import PicturesManager

class Dataset:

  def __init__(self, path_dataset):
    """
      Init the dataset object.
      
      Create the dataset folder if not exist

      :param path_dataset: The path to the dataset (root)
      :type path_dataset: string 
    """
    self.path_dataset = path_dataset
    self.pictures_manager = PicturesManager(path_dataset)
    self._create_if_not_exist_dataset_folder()

  def _create_if_not_exist_dataset_folder(self):
    """
      Create the dataset folder if not exist
    """
    if not os.path.exists(self.path_dataset):
      os.makedirs(self.path_dataset)

  def add_search_to_dataset(self, label, search, number_of_results):
    """
      Add the search into the dataset label given

      :param label: The label of the search (if already exist populate)
      :type label: string

      :param search: The search to add in the dataset
      :type label: string

      :param number_of_results: The number of results of the search
      added into the dataset label
      :type number_of_results: int 
    """
    self.pictures_manager.download_pictures(
      search,
      number_of_results,
      path_to_save="{}/{}".format(self.path_dataset, label)
      )

  def add_folder_to_dataset(self, label, path_folder):
    """
      Add all the folder images into the dataset label given

      :param label: The label of the folder (if already exist populate)
      :type label: string

      :param path_folder: The folder to add in the dataset
      :type path_folder: string
    """
    pass

  def add_video_to_dataset(self, label, path_to_video, modulo):
    """
      Add the video into the dataset label given

      :param label: The label of the video (if already exist populate)
      :type label: string

      :param modulo: The modulo of image taken in the video. 
      Example: modulo = 2, one image on two will be taken
      :type modulo: int
    """
    folder_to_save='{}/{}'.format(self.path_dataset, label)
    if not os.path.exists(folder_to_save):
      os.mkdir(folder_to_save)

    basename = path.basename(path_to_video)
    name = path.splitext(basename)[0]
    name = name + '_'

    vidcap = cv2.VideoCapture(path_to_video)
    count = 0
    success = True
    while success:
      success, image = vidcap.read()

      path_to_save = "{}/{}{}.jpg".format(folder_to_save, name, count)
      count += 1
      if success and (count % modulo == 0):
        print(path_to_save)
        cv2.imwrite(path_to_save, image)     # save frame as JPEG file

  def check_if_dataset_is_valid(self):
    """
      Check if all the images are in the correct format (jpg)
      and not corrupted
    """
    pass

  def correct_dataset(self):
    """
      Remove all the problem which can cause problem.
    """
    pass

  def retrain(self, options):
    """
      Retrain the dataset with the given options.

      :param options: Options to retrain the dataset 
      (see docs form more details)
      :type modulo: dict
    """
    pass
