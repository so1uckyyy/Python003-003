# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spider.items import SpiderItem

class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[contains(@class, "movie-hover-info")]')
        print(movies)
        for movie in movies[0:10]:
            name = movie.xpath('./div/span[@class="name "]/text()')
            print(name.extract_first())
            category = movie.xpath('./div/span[contains(text(), "类型")]/parent::*/text()')
            print(category.extract()[-1].strip())
            show_time = movie.xpath('./div/span[contains(text(), "上映时间")]/parent::*/text()')
            print(show_time.extract()[-1].strip())
            item = SpiderItem()
            item['name'] = name.extract_first()
            item['category'] = category.extract()[-1].strip()
            item['show_time'] = show_time.extract()[-1].strip()
            yield item
