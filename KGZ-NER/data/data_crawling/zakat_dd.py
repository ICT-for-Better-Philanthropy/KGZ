import scrapy
from ..items import Kgz2020Item

class ZakatDompet(scrapy.Spider):
    name = 'zakatdd'
    start_urls = [
        'http://www.dompetdhuafa.org/id/layanan/detail/faq'
    ]

    def parse(self, response):

        items = Kgz2020Item()

        page_content = response.css('.container')


        for zakats in page_content:
            judul = zakats.css('strong::text').extract()
            isi = zakats.css('div::text').extract()

            items['judul'] = judul
            items['isi'] = isi

            yield items



