# -*- coding: utf-8 -*-

from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
from icrawler.examples import BaiduImageCrawler

print("Initialisation du script\n")

maRecherche = "Basil leaf"
nombreImage = 20


print("Google\n")
pathToSave = "../../images/plants/Google/"
google_crawler = GoogleImageCrawler(path_to_save=pathToSave, img_dir=maRecherche)
google_crawler.crawl(keyword=maRecherche, offset=0, max_num=nombreImage,
	date_min=None, date_max=None, feeder_thr_num=1,
	parser_thr_num=1, downloader_thr_num=4,
	min_size=(200,200), max_size=None)

print("Bing\n")
pathToSave = "../../images/plants/Bing/"
bing_crawler = BingImageCrawler(path_to_save=pathToSave, img_dir=maRecherche)
bing_crawler.crawl(keyword=maRecherche, offset=0, max_num=nombreImage,
  feeder_thr_num=1, parser_thr_num=1,
  downloader_thr_num=4,
	min_size=(200,200), max_size=None)

print("Fin du script")
