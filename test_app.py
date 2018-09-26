import unittest
import json

from api.__init__ import create_app


class Testendpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_get(self):
        respond = self.client.get('/orders/api/v1/orders',
                                  headers={"content-type": "application/json"})

    def test_get(self):
        respond = self.client.get('/orders/api/v1/orders/<int:order_id',
                                  headers={"content-type": "application/json"})

    def test_post(self):
        respond = self.client.post('/orders/api/v1/orders',
                                   headers={"content-type": "application/json"})

    def test_put(self):
        respond = self.client.put('/orders/api/v1/orders/<int:order_id>',
                                  headers={"content-type": "application/json"})

    def test_delete(self):
        respond = self.client.delete('/orders/api/v1/orders/<int:order_id>',
                                     headers={"content-type": "application/json"})
