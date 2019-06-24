# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy import signals
import scrapy
from selenium import webdriver
import time


class AreaSpiderMiddleware(object):
    def process_request(self, request, spider):
        # 指定谷歌浏览器路径
        self.driver = webdriver.Firefox()
        if request.url != 'https://www.aqistudy.cn/historydata/':
            print(request.url)
            self.driver.get(request.url)
            time.sleep(2)
            html = self.driver.page_source
            self.driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8',
                                            request=request)