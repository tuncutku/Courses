from models.item import Item
from psycopg2.extras import Json

ipad = Item(
    "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-64gb/p3834601",
    "p",
    {"class": "price price--large"},
)

ipad.save()

# Check the item is in MongoDB
#   Use correct database
#   Find colleciton
#   Check item

items_loaded = Item.all()
print(items_loaded)
print(items_loaded[0].load_price())
