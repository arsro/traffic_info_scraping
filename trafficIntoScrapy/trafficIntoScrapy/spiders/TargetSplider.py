# coding: utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from trafficIntoScrapy.items import TrafficInfoItem

class TargetSplider(CrawlSpider):
        # scrapyをCLIから実行するときの識別子
        name = 'traffic'
        # spiderに探査を許可するドメイン
        allowed_domains = ["transit.yahoo.co.jp"]
        # 起点(探査を開始する)URL
        start_urls = ["http://transit.yahoo.co.jp/traininfo/area/6/#item306"]
        # LinkExtractorの引数で特定のルール(例えばURLにnewを含むページのみスクレイプするなど)を指定可能だが、今回は全てのページを対象とするため引数はなし
        # Ruleにマッチしたページをダウンロードすると、callbackに指定した関数が呼ばれる
        # followをTrueにすると、再帰的に探査を行う
        rules = [Rule(LinkExtractor(allow=('detail',)), callback='parse_pageinfo', follow=False)]
        
        def parse_pageinfo(self, response):
                sel = Selector(response)
                item = TrafficInfoItem()
                #item['URL'] = response.url
                # ページのどの部分をスクレイプするかを指定
                #item['title'] = sel.xpath('/html/head/title/text()').extract()
                item['index'] = sel.xpath('//h1[@class="title"]/text()').extract()
                item['contents'] = sel.xpath('//div[@id="mdServiceStatus"]/dl/dt/text()').extract()
                return item
                
        
