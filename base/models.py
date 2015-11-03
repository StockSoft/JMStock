from django.db import models

# Create your models here.

class KLine(models.Model):
    # { "_id" : ObjectId("56121e07d4abca003b63feca"), "volume" : 1290.64, "v_ma10" : 1174.78, "v_ma20" : 905.99, "ma5" : 15.536, "price_change" : 0.01, "v_ma5" : 1189.93, "p_change" : 0.06, "high" : 15.53, "ma20" : 15.5485, "low" : 15.44, "close" : 15.53, "open" : 15.52, "ma10" : 15.51, "turnover" : 0.04 }
    code = models.CharField(max_length=12)
    ktype = models.CharField(max_length=10)
    timestamp = models.IntegerField()
    volume = models.FloatField()
    v_ma10 = models.FloatField()
    ma5 = models.FloatField()
    price_change = models.FloatField()
    v_ma5 = models.FloatField()
    p_change = models.FloatField()
    high = models.FloatField()
    ma20 = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    open = models.FloatField()
    ma10 = models.FloatField()
    turnover = models.FloatField()

class KLineCodeList(models.Model):
    code = models.CharField(max_length=12)
    ktype = models.CharField(max_length=10)
    start = models.CharField(max_length=36)
    end = models.CharField(max_length=36)
    last_update = models.IntegerField()
