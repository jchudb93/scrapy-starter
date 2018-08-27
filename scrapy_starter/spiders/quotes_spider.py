import scrapy


class QuotesSpider(scrapy.Spider):

    name = "quotes"

    def start_requests(self):
        urls = [
            "https://www.sunarp.gob.pe/ConsultaVehicular/",
            "https://www.sunarp.gob.pe/seccion/servicios/detalles/0/c3.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'

        with open(filename, 'wb') as f:

            f.write(response.body)

        self.log(f'Saved file {filename}')
