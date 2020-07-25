from typing import Dict, List
from bs4 import BeautifulSoup
import requests
import re

from models.model import Model
from common.database import Database


class Item(Model):
    collection = "item"

    def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None):
        super().__init__()
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self._id = _id

    def __repr__(self):
        return f"<Item {self.url}>"

    def load_price(self) -> float:
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d+\.\d+)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)
        return self.price

    def save(self) -> None:
        Database.insert_item(self.url, self.tag_name, self.query)

    def remove():
        pass
