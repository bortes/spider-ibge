import scrapy
from ibge.items import MunicipioItem


class MunicipiosSpider(scrapy.Spider):
    name            = 'IBGE'
    allowed_domains = ['ibge.gov.br']
    start_urls      = ['https://www.ibge.gov.br/explica/codigos-dos-municipios.php']
    custom_settings = {
        'ITEM_PIPELINES': {
            'ibge.pipelines.MunicipiosPorEstadoPipeline': 300
        }
    }

    def parse(self, response):
        for estado in response.css('.container-uf'):
            uf = estado.css('thead::attr(id)').extract_first()

            if uf is None:
                continue

            municipios = estado.css('tr.municipio')

            self.logger.info(f'encontrado {len(municipios)} cidades para o estao de {uf}')

            for municipio in municipios:
                codigo = municipio.css('.numero::text').extract_first()
                nome   = municipio.css('a::text').extract_first()
                link   = estado.css('a::attr(href)').extract_first()

                yield MunicipioItem(uf=uf, codigo=codigo, nome=nome, link=link)
