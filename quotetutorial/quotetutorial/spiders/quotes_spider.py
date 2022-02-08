import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"  # This is our spider

    start_urls = [
        'https://quotes.toscrape.com/'  # Do not change the name a these two variables because (scrapy.Spider) class expect these two variables
    ]
    def parse(self, response):         # self --> (It is self instance or object) response-->It is basically contains the sourse code of our website that we want to scrap
        # title = response.css('title::text').extract()
        # yield {'titletext':title}      # Do not change the name of parse function
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tags = quotes.css(".tag::text").extract()
            yield {
                "title" : title,
                "author" : author,
                "tags" : tags
            }