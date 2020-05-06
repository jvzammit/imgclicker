
from django.db import models


class Item(models.Model):
    item_id = models.IntegerField()
    title = models.CharField(max_length=124)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f'[{self.item_id}] {self.title}'
