# -*- coding: utf-8 -*-

import os
from os import *
import cv2

def extract_frame_from_video(path_to_video, frequence, path_to_save):

  if not os.path.exists(path_to_save):
    os.mkdir(path_to_save)

  basename = path.basename(path_to_video)
  name = path.splitext(basename)[0]
  name = name + '_'

  vidcap = cv2.VideoCapture(path_to_video)
  count = 0
  success = True
  while success:
    success, image = vidcap.read()

    path_to_save_image = "{}/{}{}.jpg".format(path_to_save, name, count)
    count += 1
    if success and (count % frequence == 0):
      print(path_to_save_image)
      cv2.imwrite(path_to_save_image, image)     # save frame as JPEG file
