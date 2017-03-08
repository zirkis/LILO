# -*- coding: utf-8 -*-

from deep_learning import crawl

if __name__ == '__main__':

	crawl('flickr','basil,leaf',300,'data_on_preparation/basil/')
	crawl('flickr','mint,leaf',300,'data_on_preparation/mint/')
	crawl('flickr','thymes,plant',300,'data_on_preparation/thyme/')
	crawl('flickr','sage,leaf',300,'data_on_preparation/sage/')
	crawl('flickr','coriander,leaf',300,'data_on_preparation/coriander/')
	crawl('flickr','sun, flower',300,'data_on_preparation/sunflower/', color_code=4)
	crawl('flickr','parsley,leaf',300,'data_on_preparation/parsley/')
	crawl('flickr','purslane, flower',300,'data_on_preparation/purslaneflower/', color_code=4)
	crawl('flickr','petunia',300,'data_on_preparation/petunia/', color_code='a')
