from typing import List, Dict
from common.database import Database
from models.item import Item
from models.model import Model


class Alert(Model):
    collection = "alert"

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        super().__init__()
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self._id = _id

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self) -> None:
        if self.item.price < self.price_limit:
            print(
                f"Item {self.item} has reached a price under {self.price_limit}. Latest price: {self.item.price}."
            )

    def save():
        pass

    def remove():
        pass
