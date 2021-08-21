# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyMoocItem(scrapy.Item):
    name=scrapy.Field()
    department=scrapy.Field()
    date=scrapy.Field()
    pass

class InfoItem(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    department=scrapy.Field()
    date=scrapy.Field()
    procontent=scrapy.Field()
    goal=scrapy.Field()
    achievements=scrapy.Field()
    requests=scrapy.Field()
    pass
