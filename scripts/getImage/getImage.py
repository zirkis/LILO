# -*- coding: utf-8 -*-

from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
from icrawler.examples import BaiduImageCrawler


def getImages(pathToSave, mySearch, numberOfPictures):

	google_crawler = GoogleImageCrawler(path_to_save=pathToSave, img_dir=mySearch)
	google_crawler.crawl(keyword=mySearch, offset=0, max_num=numberOfPictures,
		date_min=None, date_max=None, feeder_thr_num=1,
		parser_thr_num=1, downloader_thr_num=4,
		min_size=(200,200), max_size=None)
	"""
	print("Bing\n")
	pathToSave = "../../images/plants/Bing/"
	bing_crawler = BingImageCrawler(path_to_save=pathToSave, img_dir=maRecherche)
	bing_crawler.crawl(keyword=maRecherche, offset=0, max_num=nombreImage,
	  feeder_thr_num=1, parser_thr_num=1,
	  downloader_thr_num=4,
		min_size=(200,200), max_size=None)
	"""

if __name__ == '__main__':
	print("Initialisation du script\n")

	aromaticsSearch = ["Basil leaf",
									 "Parsley leaf",
									 "Mint leaf",
									 "Thyme leaf",
									 "Thai basil leaf",
									 "Purple basil leaf"]

	flowersSearch = ["Sunflower leaf",
									"Purslane leaf",
									"Petunia leaf"]

	fruitsAndVegetables = ["salad",
												"cherry",
												"tomato",
												"pepper mini"]

	search = {'aromatics': aromaticsSearch,
						'flowers': flowersSearch,
						'fruitsAndVegetable': fruitsAndVegetables}

	numberOfPictures = 30
	pathToSave = "../../images/plants/"


	for categorie, searches in search.items():
		for specie in searches:
			getImages(pathToSave + categorie + '/', specie, numberOfPictures)						 

	print("Fin du script\n")
