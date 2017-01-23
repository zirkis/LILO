# -*- coding: utf-8 -*-

from deep_learning import extract_frame_from_video

if __name__ == '__main__':
  
  path_to_save = 'data_on_prepare_example'
  path_to_videos = "../../data_on_prepare/videos"

  videos = [{"name": "Basilic_1.m4v", "label": "basil"}]

  for video in videos:
    extract_frame_from_video('{}/{}'.format(path_to_videos, video['name']),
    	20, '{}/{}'.format(path_to_save, video['label']))
