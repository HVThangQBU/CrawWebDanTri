
import scrapy
class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'tocao'
    start_urls = [
         #'http://quotes.toscrape.com/',
        'https://dantri.com.vn/xa-hoi/thuc-hu-thong-tin-6-van-con-vit-chet-duoi-o-nghe-an-20221006110349314.htm',
    ]
    def parse(self, response):
        title = response.xpath('.//h1[@class="title-page detail"]/text()').get()
        #content = response.xpath('.//div[@class="singular-content"]/p/text()').getall(),
        content = response.xpath(".//*[@class='singular-container']").getall()

        title2 = str(title)
        content2 = str(content)
        content3 = content2.strip(", ['']").replace(',', '')
        ct4 = content3.split( "</article>",1 )
        print('tieu de: ', title2.strip().replace(',',''))
        print('content: ',ct4 )
        print("===========")
        print(ct4[0] + '</article>')
        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))





