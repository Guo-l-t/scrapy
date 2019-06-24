# scrapy

1. scrapy startproject projectname
2.scrapy crawl projectname
3.  items.py 负责数据模型的建立，类似于实体类。存放的是我们要爬取数据的字段信息。
    middlewares.py 自己定义的中间件。
    pipelines.py 负责对spider返回数据的处理。
    settings.py 负责对整个爬虫的配置。
    spiders目录 负责存放继承自scrapy的爬虫类。
    scrapy.cfg scrapy基础配置
    
 https://www.cnblogs.com/zengsf/p/10050414.html
 https://blog.csdn.net/zhusongziye/article/details/80342781
 https://blog.csdn.net/weixin_42350948/article/details/82593409
 https://cloud.tencent.com/developer/article/1351665
 https://movie.douban.com/tag/#/?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97
