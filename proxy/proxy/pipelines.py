# -*- coding: utf-8 -*-

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from scrapy.exceptions import DropItem

from proxy.db.models import Proxy, Base
from proxy.items import ProxyItem


class ProxyPipeline(object):
  def __init__(self):
    basename = 'proxydb'
    self.engine = create_engine('sqlite:///{}'.format(basename), echo=False)
    if not os.path.exists(basename):
      Base.metadata.create_all(self.engine)

  def process_item(self, item, spider):
    if isinstance(item, ProxyItem):
      proxy = Proxy(**item)
      self.session.add(proxy)
    return item

  def close_spider(self, spider):
    self.session.commit()
    self.session.close()

  def open_spider(self, spider):
    self.session = Session(bind=self.engine)







