import unittest
import json
from api.v1.app import app


class Testendpoints(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()

  def test_get_orders(self):
    request = self.client.get('/orders/api/v1/orders/',
                              headers={"content-type": "application/json"})
    self.assertEqual(request.status_code, 200)

  def test_get_order(self):
    request = self.client.get('/orders/api/v1/orders/1/',
                              headers={"content-type": "application/json"})
    self.assertEqual(request.status_code, 200)

  def test_create_order(self):
    data = {"meal": "codebalaa",
            "price": 750,
            "description": "lit",
            "address": "here",
            "delivered": False
            }
    request = self.client.post("/orders/api/v1/orders/",
                               data=json.dumps(data), headers={"content-type": "application/json"})
    print(request.data)
    self.assertEqual(request.status_code, 201)

  def test_update_order(self):
    data = {'delivered': False}
    request = self.client.put('/orders/api/v1/orders/2/',
                              data=json.dumps(data), headers={"content-type": "application/json"})
    print(request.data)
    self.assertEqual(request.status_code, 200)

  def test_delete_order(self):
    request = self.client.delete('/orders/api/v1/orders/2/',
                              headers={"content-type": "application/json"})

    self.assertTrue(request.status_code, 200)
