# -*- coding: utf-8 -*-

from deep_learning import crawl

if __name__ == '__main__':

	path_to_save = 'data_example'

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

	number_of_results = 5

	for label, search in searchies.iteritems():
		crawl('google', search, number_of_results, '{}/{}'.format(path_to_save, label))			
