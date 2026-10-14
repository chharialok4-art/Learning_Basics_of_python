class CustomHeaderMiddleware:
    def process_request(self, request, spider):
        request.headers["X-Project"] = "ScrapyDemo"
        return None
# This class must be enabled in the project's settings.py before Scrapy will use it. because its a downloader middleware.
