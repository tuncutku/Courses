from models.item import ItemModel
from tests.

class ItemTest(base_test):
    def test_crud(self):
        item = ItemModel("test", 19.99)

        self.