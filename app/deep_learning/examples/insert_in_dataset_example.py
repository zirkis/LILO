# -*- coding: utf-8 -*-

from deep_learning import insert_in_dataset

if __name__ == '__main__':
	label = 'basil'
	path_to_add = 'data_on_prepare_example/basil'
	path_dataset = 'dataset_example'

	insert_in_dataset(label, path_to_add, path_dataset)
