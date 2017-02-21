# -*- coding: utf-8 -*-

from deep_learning import crawl, extract_frame_from_video

if __name__ == '__main__':

	path_to_save = 'data_on_prepare_example'
	path_to_videos = "../../data_on_prepare/videos"

	searchies = {"basil": "Basil leaf"}
	"""
	# POPULATE WITH SEARCHIES 
	aromatics_searchies = {"basil": "Basil leaf",
									 "parsley": "Parsley leaf",
									 "mint": "Mint leaf",
									 "thyme": "Thyme leaf",
									 "thai basil": "Thai basil leaf",
									 "purple basil": "Purple basil leaf"}

	flowers_searchies = {"sunflower": "Sunflower",
									"purslane": "Purslane",
									"petunia": "Petunia"}

	fruits_and_vegetables_searchies = {"lettuce": "lettuce",
												"cherry": "cherry",
												"tomato": "tomato",
												"pepper mini": "pepper mini"}

	searchies = dict(aromatics_searchies.items() +
		flowers_searchies.items() +
		fruits_and_vegetables_searchies.items()) 
	"""
	number_of_results = 100

	for label, search in searchies.iteritems():
		crawl('flickr', search, number_of_results, '{}/{}'.format(path_to_save, label))

	"""
	# POPULATE WITH VIDEOS
  videos = [{"name": "Basilic_1.m4v", "label": "label1"}]

  for video in videos:
    extract_frame_from_video('{}/{}'.format(path_to_videos, video['name']),
    	20, '{}/{}'.format(path_to_save, video['label']))
"""