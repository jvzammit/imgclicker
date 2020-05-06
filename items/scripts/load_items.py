
import json

from items.models import Item


FILE_PATH = 'items/files/items_v2.json'


def insert_item(data_item):
    Item.objects.create(
        item_id=data_item['id'],
        title=data_item['title'],
        description=data_item['description'],
        image_url=data_item['imageUrl'],
    )


def run():
    items_json = json.loads(open(FILE_PATH).read())
    for data_item in items_json['items']:
        insert_item(data_item)
    print('Data loaded.')
