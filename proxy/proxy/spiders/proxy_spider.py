import re

import scrapy
from proxy.items import ProxyItem


class ProxySpider(scrapy.spiders.CrawlSpider):
  name = 'proxy_spider'
  # allowed_domains = ['proxylist.hidemyass.com']
  # start_urls = ['http://proxylist.hidemyass.com/']

  def start_requests(self):
    urls = ['http://proxylist.hidemyass.com/', ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    section = response.xpath('//section[contains(@class, "proxy-results")]')
    table = section.xpath('.//div/table[contains(@class, "hma-table")]')
    head = table.xpath('.//thead')
    body = table.xpath('.//tbody')

    ip_index = next(i for i, v in enumerate(head.css('th'))
                    if 'IP Address' in v.xpath('text()').extract())
    port_index = next(i for i, v in enumerate(head.css('th'))
                      if 'Port' in v.xpath('text()').extract())

    for tr in body.css('tr'):
      port = tr.css('td')[port_index].xpath('text()').extract_first().split()[0]

      ip_elem = tr.css('td')[ip_index].css('span')
      ip_style = ip_elem.xpath('child::style').extract_first()

      wrong_classes = [i.lstrip('.').split('{')[0]
                       for i in ip_style.split() if 'display:none' in i]
      ip_text = ''.join(tr.css('td')[ip_index].css('span').extract())

      ip_text = re.sub('\n', '', ip_text)
      ip_text = re.sub('.+<style>.+<\/style>', '', ip_text)
      ip_text = re.sub('<div style="display:none">.{0,3}<\/div>', '', ip_text)
      ip_text = re.sub('<span><\/span>', '', ip_text)
      ip_text = re.sub('<span style="display:none">.{0,3}<\/span>', '', ip_text)

      for wrong_class in wrong_classes:
        ip_text = re.sub('<span class="{}">{}<\/span>'.format(wrong_class, '.{0,3}'), '', ip_text)

      ip_text = re.sub('<span style="display: inline">', '', ip_text)
      ip_text = re.sub('<span class=".{0,4}">', '', ip_text)
      ip_text = re.sub('</span>', '', ip_text)
      ip_address = ip_text.split()[0]

      yield ProxyItem(port=port, ip_address=ip_address)







