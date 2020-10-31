from unittest import TestCase
from models.item import ItemModel

class ItemTests(TestCase):
    def test_create_item(self):
        item = ItemModel("test", 19)

        self.assertEqual(item.name, "test", "test name is not working")
        self.assertEqual(item.price, 19, "test price is not working")

    def test_item_json(self):
        item = ItemModel("test", 19)
        expected_output = {
            "name": "test",
            "price": 19
        }
        self.assertEqual(item.json(), expected_output, "json is not same")
