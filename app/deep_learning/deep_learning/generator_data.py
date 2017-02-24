# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np

def delete_image_if_exist(image_path):
  try:
    os.remove(image_path)
    print("Image: {} deleted".format(data_path))
  except OSError:
    pass

def image_to_feature_vector(image, size=(64, 64)):
  # resize the image to a fixed size, then flatten the image into
  # a list of raw pixel intensities
  return np.array(cv2.resize(image, size).flatten()) / 255.0

def generator_data(data_paths, data_labels):
  while True:
    for (i, data_path) in enumerate(data_paths):
      image = cv2.imread(data_path)

      # If the image is corrupted delete it
      if image is None:
        delete_image_if_exist(data_path)
        continue

      data = image_to_feature_vector(image)
      data = data.reshape((1, data.shape[0]))
      label = np.array(data_labels[i]).reshape((1, data_labels[i].shape[0]))
      yield data, label
