import scrapy
from ..items import Kgz2020Item

class ZakatDirektorat(scrapy.Spider):
    name = 'zakatdir'
    start_urls = [
        'http://alazharpeduli.com/panduan-zakat'
    ]

    def parse(self, response):

        items = Kgz2020Item()

        page_content = response.css('.pst-block-main')


        for zakats in page_content:
            judul = zakats.css('.redactor-inline-converted::text').extract()
            isi = zakats.css('p::text').extract()

            items['judul'] = judul
            items['isi'] = isi

            yield items



