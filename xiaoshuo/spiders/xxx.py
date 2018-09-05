# -*- coding: utf-8 -*-
import scrapy


class XxxSpider(scrapy.Spider):
    name = 'xxx'
    allowed_domains = ['baidu.com']
    start_urls = ['http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html']

    def parse(self, response):
        aa=response.xpath('/html/body/div[1]/nav/div/div[2]/ul/li/a/@href').extract()
        for item in aa:
            f=open('aaa.txt','ab')
            f.write(item)
