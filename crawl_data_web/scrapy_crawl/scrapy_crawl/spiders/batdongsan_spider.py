
from urllib.request import Request
from ..items import BatdongsanDataItem
import scrapy
from scrapy.crawler import CrawlerProcess



url= 'https://batdongsan.com.vn/nha-dat-ban'


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_donains =['batdongsan.com.vn']
    start_urls = [url]
    # HTTPERROR_ALLOWED_CODES  =[404]
    # handle_httpstatus_list = [403]
    
    def start_requests(self):
        headers= {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'origin': 'https://batdongsan.com.vn',
            'referer': 'https://batdongsan.com.vn/nha-dat-ban',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            # 'content-length': '0',
            # 'content-type': 'application/json',
            # 'cookie': 'cf_clearance=ksd3ZfzcOjHBEl2EAnYpqwWHNCP114uqa8F1g8OqKcc-1662733029-0-250; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%22d0e72856-a2d6-40b3-ba61-50cbfaba8212%22%2C%22expireDate%22%3A%222023-09-09T21%3A17%3A09.5902086Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22328856a5-b0c9-4653-902c-7d5b938361e6%22%2C%22expireDate%22%3A%222023-09-09T21%3A17%3A09.6140731Z%22%7D; _gcl_au=1.1.1973913773.1662733079; _fbp=fb.2.1662733079222.1136194958; _uidcms=1662733377626647359; __RC=4; __R=1; __tb=0; __IP=1984235420; __UF=-1; _hjSessionUser_1708983=eyJpZCI6IjhmNjgwNjY4LTFkMDAtNTllYy04NmY1LTUxNGY4MzIwODQ1YyIsImNyZWF0ZWQiOjE2NjI3MzMwNzYxMjcsImV4aXN0aW5nIjp0cnVlfQ==; BUTTON_MORE_ACTIONS=1; _pbjs_userid_consent_data=3524755945110770; cto_bidid=XU4p1V9uMjlGVUdFMkthcDUlMkZiVnZRJTJGc0xhN2dHbjZYTDEyeDh4dWlNRW5HTkFCQ1gycGsxdkNXcTJxOEp1S0d4Q2lDMW54d003Z2RQUkE2eDF0amFvOVR2c1Z1Q2RwQnFuRmdvWFg1NjdPQU9rcnBrNXRHaWRHWWNPdzMxeU1EWCUyQkFiYw; cto_bundle=yfHorl9uVUJFNE90c1FpZlQwYmpXVDNtYnVCTzQzWm4wRlRsMWVXa0FWV1hJTUZ2eWQ5blJHa0hieHBjdHFnYjRoNFZrTSUyRm5GYmtDSDlmdU9rM3dtOFVqRjN3dXhtSW15cTBYQ0wxeFJUM0laJTJCOXdDZ09QMUkwcTF6cWlRV0l3Rm1qeVJ4Q09NVE43ejRBOUZUUGNmMmM2c3lnJTNEJTNE; _gid=GA1.3.807667632.1664807174; con.ses.id=95ca5e10-7cef-4594-90b1-564997726200; __cfruid=1fb7763017e78a669984e4e76ec730ce3dd5759d-1664890479; __gpi=UID=000009a29ee8fdbc:T=1662733030:RT=1664890480:S=ALNI_Mbr82f-DyAGeTlVpzIH6o4IqOfo2w; _hjIncludedInSessionSample=0; _hjSession_1708983=eyJpZCI6IjYwMmExZDZlLTUxMzQtNGIxMi1hYzBkLWI0NGIzNDdkMzE5YyIsImNyZWF0ZWQiOjE2NjQ4OTA1MjEyODUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7fSwidXNlcklkIjpudWxsfQ==; USER_PRODUCT_SEARCH=38%7C324%7CSG%7C61%7C5849%7C0%7C2711%2C34998631; _gat_UA-3729099-1=1; _ga_HTS298453C=GS1.1.1664890520.41.1.1664891729.10.0.0; __cf_bm=mrS.sNb2IbEJhyEGv8jPEmIlgSLWn_e2nav.fXBb.gI-1664891689-0-Aa7xx3FxoPcwurYhzbwE6w7Ji3zNysZHiIuDdLxMAH3lps7eyFv9SaumDCYqTtban+5Zedmn+jrIG7R+rXEgNIXzbU3H5oYt+xiM+9J7EksDN9nIrZEB0o83adWnzIKOD+hrLmKPK94J0t0M/MRgNVIABnmyDVQvA/XD4/U6KFBw; _ga=GA1.3.1737957892.1662733076; __gads=ID=7a85f595dccdf15b:T=1662733030:S=ALNI_MadYV3eVTZVrXZdknS0ylhxSdKJaA',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            }
        for urls in self.start_urls:
            yield scrapy.Request(urls, headers=headers)

    def parse(self, response):
        for page_link in response.xpath('//a[@class="js__product-link-for-product-id"]/@href').getall():
            proj_page = response.urljoin(page_link)
            yield scrapy.Request(proj_page, callback=self.parse_single_proj)

            next_page_url = response.css("a.re__pagination-icon")[-1].attrib
            if next_page_url is not None:
                next_page_link = response.urljoin(next_page_url.get('href'))
                yield scrapy.Request(next_page_link, callback=self.parse) 


    def parse_single_proj(self, response):
        info_department = response.xpath('//div[@class="re__pr-info pr-info js__product-detail-web"]')
        item = BatdongsanDataItem(
            web = "batdongsan",
            department = info_department.xpath('//h1[@class="re__pr-title pr-title js__pr-title"]/text()').get(),
            address = info_department.xpath('//span[@class="re__pr-short-description js__pr-address"]/text()').get(),
            estate = info_department.xpath('//div[@class="re__section-body re__border--std js__section-body"]/span[@class="re__pr-specs-product-type"]/text()').get(), 
            price = info_department.xpath('//div[@class="re__pr-short-info-item js__pr-short-info-item"]/span[@class="value"]/text()').get(),
            area = info_department.xpath('//div[@class="re__pr-short-info-item js__pr-short-info-item"]/span[@class="value"]/text()')[1].getall(),
            group = info_department.css('div.re__pr-specs-content-item span::text').getall()  
        )
        yield item
