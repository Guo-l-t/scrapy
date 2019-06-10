# scrapy

1. scrapy startproject projectname
2.scrapy crawl projectname
3.  items.py 负责数据模型的建立，类似于实体类。存放的是我们要爬取数据的字段信息。
    middlewares.py 自己定义的中间件。
    pipelines.py 负责对spider返回数据的处理。
    settings.py 负责对整个爬虫的配置。
    spiders目录 负责存放继承自scrapy的爬虫类。
    scrapy.cfg scrapy基础配置
