# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass


class ScrapyCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

@dataclass
class RetiDataItem:
    web: str
    address : str
    department : str
    estate: str
    price : str
    area : str
    group : dict

@dataclass
class AlonhadatDataItem:
    web: str
    address : str
    department : str
    estate: str
    price : str
    area : str
    group : dict

@dataclass
class CafelandDataItem:
    web: str
    address : str
    department : str
    estate: str
    price : str
    area : str
    group : list

@dataclass
class BatdongsanDataItem:
    web: str
    address : str
    department : str
    estate: str
    price : str
    area : str
    group : list