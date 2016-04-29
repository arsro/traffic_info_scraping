#!/bin/bash
rm /var/www/html/scraping/output/*.json
cd /var/www/html/scraping/trafficIntoScrapy/trafficIntoScrapy/spiders/
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl traffic -o /var/www/html/scraping/output/traffic_result.json
