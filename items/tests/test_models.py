
from model_bakery import baker
from django.test import TestCase


class ItemTest(TestCase):

    def test_str(self):
        item = baker.make(
            'items.Item',
            item_id=345, title='Test Item')
        self.assertEqual(str(item), '[345] Test Item')

    def test_preview_link_endswith_preview_no(self):
        item = baker.make(
            'items.Item',
            image_url='https://cdn.nous.com/image.png')
        self.assertEqual(
            item.preview_link, 'https://cdn.nous.com/image.png/preview')

    def test_preview_link_endswith_preview_yes(self):
        item = baker.make(
            'items.Item',
            image_url='https://cdn.nous.com/image.png/preview')
        self.assertEqual(
            item.preview_link, 'https://cdn.nous.com/image.png/preview')
