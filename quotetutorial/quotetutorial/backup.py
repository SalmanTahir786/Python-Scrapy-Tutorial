import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]
    def parse(self, response):

        items = QuotetutorialItem()
        all_div_quotes = response.css("div.quote")

        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
        next_page = 'https://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
# Now using if condition to check the next page value is empty or not
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, call_back=self.parse)