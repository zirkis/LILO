# -*- coding: utf-8 -*-

from deep_learning.dataset import Dataset

if __name__ == '__main__':

	path_to_dataset = 'data_example'
	dataset = Dataset(path_to_dataset)

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

	searchies = aromatics_searchies + flowers_searchies + fruits_and_vegetables_searchies

	number_of_results = 50

	for label, search in searchies.iteritems():
		dataset.add_search_to_dataset(label, search, number_of_results)			
