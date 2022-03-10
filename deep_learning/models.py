from unittest.loader import VALID_MODULE_NAME
from django.db import models

# Create your models here.


class sale_market_viz(models.Model):
    date = models.CharField(max_length=10)
    trade_code = models.CharField(max_length=10)
    high = models.CharField(max_length=10)
    low = models.CharField(max_length=10)
    open = models.CharField(max_length=10)
    close = models.CharField(max_length=10)
    volume = models.CharField(max_length=10)

