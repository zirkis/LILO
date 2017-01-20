# -*- coding: utf-8 -*-

from icrawler.examples import GoogleImageCrawler

def crawl(type_crawler, search, number_of_results, path_to_save):

	if type_crawler == 'flickr':
		pass
	else:
		google_crawler = GoogleImageCrawler(path_to_save, search)
		google_crawler.crawl(
			keyword=search,
			offset=0,
			max_num=number_of_results,
			date_min=None,
			date_max=None,
			feeder_thr_num=1,
			parser_thr_num=1,
			downloader_thr_num=4,
			min_size=(200,200),
			max_size=None)
