
import scrapy
from scrapy.item import Item, Field
class CrawBaoDanTri(scrapy.Item):
    danhmuc = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    timeupdate = scrapy.Field()
    url = scrapy.Field()
    tag = scrapy.Field()
    pass



# class Itemdb(scrapy.Item):
#     name = scrapy.Field();
#     url = scrapy.Field();
#     image = scrapy.Field();
#     desciption = scrapy.Field();
#     category = scrapy.Field();
#     rating = scrapy.Field();
#     link_trailer = scrapy.Field();
#     actors = scrapy.Field();
#     length = scrapy.Field();
#     date  = scrapy.Field();
#     genres = scrapy.Field();
#     creator = scrapy.Field();
#     story_line = scrapy.Field();
#     country = scrapy.Field();
#     lenguage = scrapy.Field();
#     production_campany = scrapy.Field();


