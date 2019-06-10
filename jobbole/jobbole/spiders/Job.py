# -*- coding: utf-8 -*-
import scrapy
from jobbole.items import JobboleItem


class MeijuSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):

        jobs = response.xpath('// *[ @ id = "archive"]/div[@class="post floated-thumb"]')
        for j in jobs:
            item = JobboleItem()
            item['title'] = j.xpath('./div[2]/p[1]/a[1]/text()').extract()
            yield item

        next_page = response.xpath('//*[@id="archive"]/div[21]/a[4]/@href').extract() [0] #下一页链接
        if next_page is not None:  # 判断是否存在下一页
            next_page = response.urljoin(next_page)
            yield scrapy.http.Request(next_page, callback=self.parse, dont_filter=True)  #提交给parse继续抓取下一页