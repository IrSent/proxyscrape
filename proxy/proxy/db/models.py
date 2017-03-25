from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Proxy(Base):
  __tablename__ = 'proxy'

  id =         Column(Integer, primary_key=True)
  ip_address = Column(String(64))
  port =       Column(String(8))

  def __init__(self, ip_address=None, port=None):
    self.ip_address = ip_address
    self.port = port

  def __repr__(self):
    out = '<Proxy: id="{id}", ip_address="{ia}", port="{port}">'
    return out.format(self.id, self.ip_address, self.port)
