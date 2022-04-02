import json
from flask import jsonify

from ..model.item import Item


def retrieve_item(name):
    for item in search_db():
        if name == item['name']:
            return item
    raise NameError("Item not found")


def create_item(name, price):
    if item_exists(name):
        raise NameError("Item already exists")
    item = Item(name, price)
    # read the entire file, append the new item, write the file
    # inefficient, but it's a prototype, could easily be hooked up to a mongodb database
    with open('mock_database.json') as f:
        items_list = json.load(f)
    items_list.append(item.__dict__)
    with open('mock_database.json', 'w') as f:
        json.dump(items_list, f, indent=4)


def remove_item():
    return ""


# helpers
def search_db():
    with open('mock_database.json') as f:
        db = json.load(f)  
        for i in db:
            yield i
            

def item_exists(name):
    for item in search_db():
        if name == item['name']:
            return True
    return False