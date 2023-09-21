from django.db import models

class Item(models.Model):

    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=40)
    price = models.CharField(max_length=10)
    qty = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item