import scrapy
class Products_fetch(scrapy.Spider):
    name= "digital products"
    start_urls=["https://www.digital_products.com"]
    def parse(self,response):
        products = response.css("div.product")
        for item in products:
            yield{
                "name":item.css("h2.name::text"),
                "price":item.css("span.price::text")
            }

class New_products(scrapy.Spider):
    name="New Products"
    allowed_url=["httpd://www.sub_product_list.com"]
    start_urls=["https://www.new_product.com"]
    def parse(self,response):
        products=response.css("div.product")
        for item in products:
            yield{
                "name":item.css("h2.name::text"),
                "price":item.css("span.price::text")
            }