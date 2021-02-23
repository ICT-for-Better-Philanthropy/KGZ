import scrapy
from ..items import Kgz2020Item

class ZakatRumah(scrapy.Spider):
    name = 'zakatrumah'
    start_urls = [
        'https://www.rumahzakat.org/en/zakat/zakat-penghasilan/',
        'https://www.rumahzakat.org/en/zakat/zakat-perdagangan/',
        'https://www.rumahzakat.org/en/zakat/zakat-emas-dan-perak/',
        'https://www.rumahzakat.org/en/zakat/zakat-fitrah/',
        'https://www.rumahzakat.org/en/zakat/zakat-hadiah/',
        'https://www.rumahzakat.org/en/zakat/zakat-pertanian/',
        'https://www.rumahzakat.org/en/zakat/zakat-simpanan/',

    ]

    def parse(self, response):

        items = Kgz2020Item()

        page_content = response.css('body')


        for zakats in page_content:
            judul = zakats.xpath("//h1/text()").extract()
            isi = zakats.css('p::text').extract()

            items['judul'] = judul
            items['isi'] = isi

            yield items



