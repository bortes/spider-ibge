# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from scrapy.exporters import CsvItemExporter


class MunicipiosPorEstadoPipeline:
    def open_spider(self, spider):
        self.directory = os.path.join(spider.settings.get('BOT_OUTPUT'), spider.name.lower())

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        self.exporters = {}
        self.openfiles = {}

    def close_spider(self, spider):
        for exporter in self.exporters.values():
            exporter.finish_exporting()

        for openfile in self.openfiles.values():
            openfile.close()

    def process_item(self, item, spider):
        item['uf']   = item['uf'].upper()
        item['nome'] = item['nome'].upper()

        uf = item['uf']

        if uf not in self.exporters:
            filename = os.path.join(self.directory, f'{spider.name.lower()}.{uf}' + '.csv')

            openfile = open(filename, 'wb')

            exporter = CsvItemExporter(openfile, delimiter=';')
            exporter.start_exporting()

            self.exporters[uf] = exporter
            self.openfiles[uf] = openfile
        else:
            exporter = self.exporters[uf]

        exporter.export_item(item)

        return item
