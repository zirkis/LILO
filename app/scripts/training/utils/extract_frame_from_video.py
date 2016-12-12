# -*- coding: utf-8 -*-

import os
from os import *
import cv2


def extract_frame_from_video(pathToVideo, folderToSave="../../../data_on_prepare", modulo=1):
  if not os.path.exists(folderToSave):
    os.mkdir(folderToSave)

  basename = path.basename(pathToVideo)
  name = path.splitext(basename)[0]
  name = name + '_'

  vidcap = cv2.VideoCapture(pathToVideo)
  success,image = vidcap.read()
  count = 0
  success = True
  while success:
    success,image = vidcap.read()

    pathToSave = "{}/{}{}.jpg".format(folderToSave, name, count)
    count += 1
    if success and (count % modulo == 0):
      print(pathToSave)
      cv2.imwrite(pathToSave, image)     # save frame as JPEG file

if __name__ == '__main__':
  pathToVideo = "../../../data_on_prepare/videos/"
  folderToSave ="../../../data/"

  videos = [{"name": "Basilic_1.m4v", "folder": "basil"},
            {"name": "Basilic_2.m4v", "folder": "basil"},
            {"name": "Basilic_3.m4v", "folder": "basil"},
            {"name": "Basilic_4.m4v", "folder": "basil"},
            {"name": "Basilic_5.m4v", "folder": "basil"},
            {"name": "Basilic_6.m4v", "folder": "basil"},
            {"name": "Basilic_7.m4v", "folder": "basil"},
            {"name": "Basilic_8.m4v", "folder": "basil"},
            {"name": "Basilic_9.m4v", "folder": "basil"},
            {"name": "Basilic_10.m4v", "folder": "basil"},
            {"name": "Basilic_11.m4v", "folder": "basil"},
            {"name": "Basilic_12.m4v", "folder": "basil"},
            {"name": "Basilic_13.m4v", "folder": "basil"},
            {"name": "Basilic_14.m4v", "folder": "basil"},
            {"name": "Basilic_15.m4v", "folder": "basil"},
            {"name": "Basilic_16.m4v", "folder": "basil"},
            {"name": "Basilic_17.m4v", "folder": "basil"},
            {"name": "Basilic_18.m4v", "folder": "basil"},
            {"name": "Basilic_19.m4v", "folder": "basil"},
            {"name": "Basilic_20.m4v", "folder": "basil"},
            {"name": "Basilic_pourpre_1.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_2.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_3.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_4.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_5.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_6.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_7.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_8.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_9.m4v", "folder": "purple basil"},
            {"name": "Basilic_pourpre_10.m4v", "folder": "purple basil"},
            {"name": "Melisse_1.m4v", "folder": "melissa"},
            {"name": "Melisse_2.m4v", "folder": "melissa"},
            {"name": "Melisse_3.m4v", "folder": "melissa"},
            {"name": "Melisse_4.m4v", "folder": "melissa"},
            {"name": "Melisse_5.m4v", "folder": "melissa"},
            {"name": "Melisse_6.m4v", "folder": "melissa"},
            {"name": "Melisse_7.m4v", "folder": "melissa"},
            {"name": "Melisse_8.m4v", "folder": "melissa"},
            {"name": "Melisse_9.m4v", "folder": "melissa"},
            {"name": "Melisse_10.m4v", "folder": "melissa"},
            {"name": "Melisse_11.m4v", "folder": "melissa"},
            {"name": "Melisse_12.m4v", "folder": "melissa"},
            {"name": "Menthe_1.m4v", "folder": "mint"},
            {"name": "Menthe_2.m4v", "folder": "mint"},
            {"name": "Menthe_3.m4v", "folder": "mint"},
            {"name": "Menthe_4.m4v", "folder": "mint"},
            {"name": "Menthe_5.m4v", "folder": "mint"},
            {"name": "Menthe_6.m4v", "folder": "mint"},
            {"name": "Menthe_7.m4v", "folder": "mint"},
            {"name": "Menthe_8.m4v", "folder": "mint"}  
  ]
  for video in videos:
    extract_frame_from_video(pathToVideo + video['name'], folderToSave + video['folder'], 5)
