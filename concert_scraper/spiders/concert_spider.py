import scrapy


class ConcertSpider(scrapy.Spider):
    name = "concerts"
    start_urls = [
        "https://www.rocking.gr/agenda",
    ]

    def parse(self, response):
        i = 0
        for event in response.css(".date-box"):
            for concert in event.css(".info"):
                # groups = concert.css(".groups::text").get()
                url = concert.css("a").xpath("@href").get()
                if url is not None:
                    yield scrapy.Request(url, callback=self.get_concert_info)

                i += 1
                if i > 0:
                    return

    def get_concert_info(self, response):
        info = response.css(".agenda_info")
        for row in info.xpath("//tr"):
            key = row.xpath("td//text()")[0].extract()
            value = row.xpath("td//text()")[1].extract().strip()

            print(key)
            print(value)
            print()
