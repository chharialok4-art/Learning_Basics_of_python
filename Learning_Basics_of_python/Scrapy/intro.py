import scrapy
class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response):
        print(response.status)
        print(response.url)

class One_spider(scrapy.Spider):
    name="one_spider"
    start_urls=[
        "https://www.google.com"
        ]
    def parse(self,response):
        print(response.status)
        print(response.url)

class Testing_allowed_domains(scrapy.Spider):
    name="allowed_domains"
    allowed_domains=[
        "https://www.scrapy.com",
        "https://www.instagram.com"
    ]
    start_url=[
        "https://www.facebook.com"
    ]
    def parse(self,response):
        self.logger.info(
            "download_URL:%s",
            response.url
        )
        self.logger.info(
            "Status code:%s",
            response.status
        )

class Real_world_example:
    name="example_in_real_world"
    allowed_domains=[
        "https://www.orkut.in",
        "https://www.printese.com"
    ]
    start_url=[
        "https://www.yahoo.in"
    ]
    def parse(self,response):
        self.logged.info(
            "scraping page:%s",
            response.url
        )
        books=response.css(
            "article.product_prod"
        )
        for book in books:
            yield{
               "title": book.css().get(),
               "price": book.css().get(),
                "availbility":book.css().getall()
            }
# Its a intro for scrapy basic coding style. It not a full fladgue program except last example.
