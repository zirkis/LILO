# -*- coding: utf-8 -*-

from deep_learning import extract_frame_from_video

if __name__ == '__main__':
  
  path_to_dataset = 'data_example'

  path_to_video = "path/to/videos/"

  videos = [{"name": "video1.m4v", "label": "label1"},
            {"name": "video2.mp4", "label": "label2"}]

  for video in videos:
    extract_frame_from_video(path_to_video + video['name'], 5, path_to_save)