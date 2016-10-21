# -*- coding: utf-8 -*-

from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
from icrawler.examples import BaiduImageCrawler

print("Initialisation du script\n")

maRecherche = "Basil leaf"
nombreImage = 100

'''
print("Google\n")
google_crawler = GoogleImageCrawler(maRecherche)
google_crawler.crawl(keyword=maRecherche, offset=0, max_num=nombreImage,
	date_min=None, date_max=None, feeder_thr_num=1,
	parser_thr_num=1, downloader_thr_num=4,
	min_size=(200,200), max_size=None)
'''

print("Bing\n")
bing_crawler = BingImageCrawler(maRecherche)
bing_crawler.crawl(keyword=maRecherche, offset=0, max_num=nombreImage,
  feeder_thr_num=1, parser_thr_num=1,
  downloader_thr_num=4,
	min_size=(200,200), max_size=None)

print("Fin du script")
