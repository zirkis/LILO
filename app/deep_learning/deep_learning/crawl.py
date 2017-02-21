# -*- coding: utf-8 -*-
from datetime import date
from icrawler.examples import GoogleImageCrawler
from icrawler.examples import FlickrImageCrawler


def crawl(type_crawler, search, number_of_results, path_to_save, color_code=5):

	if type_crawler == 'flickr':
		flickr_crawler = FlickrImageCrawler('9b72938db332c2514acce33c793c2f1a', path_to_save)
		flickr_crawler.crawl(max_num=number_of_results, feeder_thr_num=1, parser_thr_num=1,downloader_thr_num=1, text=search, color=color_code)
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

crawl('flickr','basil,leaf',1000,'../../data_on_preparation/basil/')
crawl('flickr','mint,leaf',1000,'../../data_on_preparation/mint/')
crawl('flickr','thymes,plant',1000,'../../data_on_preparation/thyme/')
crawl('flickr','sage,leaf',1000,'../../data_on_preparation/sage/')
crawl('flickr','coriander,leaf',1000,'../../data_on_preparation/coriander/')
crawl('flickr','sun, flower',1000,'../../data_on_preparation/sunflower/', color_code=4)
crawl('flickr','parsley,leaf',1000,'../../data_on_preparation/parsley/')
crawl('flickr','purslane, flower',1000,'../../data_on_preparation/purslaneflower/', color_code=4)
crawl('flickr','petunia',1000,'../../data_on_preparation/petunia/', color_code='a')

