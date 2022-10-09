from ..items import AlonhadatDataItem
import scrapy
from scrapy.crawler import CrawlerProcess

URL = 'https://alonhadat.com.vn/nha-dat/can-ban.html'

class AlonhadatsSpider(scrapy.Spider):
    name = "alonhadat"
    start_urls = [URL]

    page_number = 1

    def parse(self, response):
        for page_link in response.xpath('//div[@class="ct_title"]/a/@href').getall():
            proj_page = response.urljoin(page_link)
            yield scrapy.Request(proj_page, callback=self.parse_single_proj)

        self.page_number += 1
        next_page = f'https://alonhadat.com.vn/nha-dat/can-ban/trang--{self.page_number}.html'
        if next_page is not None:
             yield scrapy.Request(next_page, callback=self.parse)
            #yield response.follow(next_page, callback=self.parse)
            
       
    def parse_single_proj(self, response):
        info_department = response.xpath('//div[@class="property"]')
        list = response.css('td::text').getall()
        lbds = list[list.index("Loại BDS") + 1]
        directions = list[list.index("Hướng")] + ": "+list[list.index("Hướng") + 1]
        streets = list[list.index("Đường trước nhà")] + ": "+list[list.index("Đường trước nhà") + 1]
        widths = list[list.index("Chiều ngang")] + ": "+list[list.index("Chiều ngang") + 1]
        longs = list[list.index("Chiều dài")] + ": "+list[list.index("Chiều dài") + 1]
        floors = list[list.index("Số lầu")] + ": "+list[list.index("Số lầu") + 1]
        bedrooms = list[list.index("Số phòng ngủ")] + ": "+list[list.index("Số phòng ngủ") + 1]
        juridicals = list[list.index("Pháp lý")] + ": "+list[list.index("Pháp lý") + 1]
        
        item = AlonhadatDataItem(
            web = "alonhadat",
            address = info_department.xpath('//div[@class="address"]/span[@class="value"]/text()').get(),
            department = info_department.xpath('//div[@class="title"]/h1/text()').get(),
            estate = lbds,
            price = info_department.css('span.price span.value::text').get(),
            area = info_department.css('span.square span.value::text').get(),
            group = {
                "direction" : directions,
                "street" : streets,
                "width" : widths,
                "long": longs,
                "floor": floors,
                "bedroom": bedrooms,
                "juridical": juridicals

            }
         )

        yield  item