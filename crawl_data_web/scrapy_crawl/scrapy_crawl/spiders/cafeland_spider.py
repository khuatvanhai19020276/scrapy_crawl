from ..items import CafelandDataItem
import scrapy
from scrapy.crawler import CrawlerProcess

URL = 'https://nhadat.cafeland.vn/nha-dat-ban/'


class CafelandSpider(scrapy.Spider):
    name = "cafeland"
    start_urls = [URL]
  
    def parse(self, response):
        for page_link in response.xpath('//div[@class="images-reales"]/a/@href').getall():
            proj_page = response.urljoin(page_link)
            yield scrapy.Request(proj_page, callback=self.parse_single_proj)

            next_page_url = response.css("ul.pagination a")[-1].attrib
            if next_page_url is not None:
                next_page_link = response.urljoin(next_page_url.get('href'))
                yield scrapy.Request(next_page_link, callback=self.parse) 


    def parse_single_proj(self, response):
        info_department = response.xpath('//div[@class="col-md-9 col-left"]')
        item = CafelandDataItem(
            web = "cafeland",
            address = info_department.xpath('normalize-space(//div[@class="infor"]/text())').get(),
            department = info_department.xpath('//div[@class="col-md-9 col-left"]/h1/text()').get(),
            estate = info_department.xpath('//div[@class="reals-house-item opt-mattien"]/span[@class="value-item"]/text()').get(), 
            price = info_department.xpath('//div[@class="col-item"]/div[@class="infor-data"]/text()').get(),
            area = info_department.xpath('//div[@class="col-item"]/div[@class="infor-data"]/text()')[1].getall(),
            group = info_department.css('div.row span::text').getall()  
        )
        yield item