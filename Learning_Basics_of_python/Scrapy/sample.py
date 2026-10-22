import scrapy
class Sample_test(scrapy.Spider):
    allowed_domains=["https://scrapy.com"]
    start_urls=["https://www.google.com"]
    def parse(self,response):
        get_data=response.css("div.product")
        print(response.status)
        print(response.url)
        for item in get_data:
            yield{
                "names":item.css("h2.name::text").get(),
                "title":item.css("span.title::text").get()
            }
        