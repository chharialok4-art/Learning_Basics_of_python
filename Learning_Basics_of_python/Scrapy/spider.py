import scrapy
class ProductSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(), # yields selects HTML elements.
                "author": quote.css("small.author::text").get()
                }
#Its a spider that is yields the text value from a html page.