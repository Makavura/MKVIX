import os
import unittest
from app.__init__ import create_app


class TestAll(unittest.TestCase):

  def setUp(self):
    self.app = create_app("test")
    self.client = self.app.test_client()
    self.app_context = self.app.app_context()
    self.app_context.push()
    self.new_order = {"meal": "Sanchezium",
                      "address": "Hunters Pub", "done": True}

  def test_get(self):
    respond = self.client.get('/api/v1/orders',
                              headers={"content-type": "application/json"})

  def test_get(self):
    respond = self.client.get('/api/v1/orders/<int:order_id',
                              headers={"content-type": "application/json"})

  def test_post(self):
    respond = self.client.post('/api/v1/orders',
                               headers={"content-type": "application/json"})

  def test_put(self):
    respond = self.client.put('/api/v1/orders/<int:order_id>',
                              headers={"content-type": "application/json"})

  def test_delete(self):
    respond = self.client.delete('/api/v1/orders/<int:order_id>',
                                 headers={"content-type": "application/json"})

