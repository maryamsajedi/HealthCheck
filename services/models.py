from django.db import models

class Service(models.Model):
    url   = models.URLField(max_length=250)
    port  = models.IntegerField()
    name  = models.CharField(max_length=50, unique = True)
    delay = models.IntegerField()
    status_code       = models.IntegerField()
    health_treshold   = models.IntegerField()
    unhealth_treshold = models.IntegerField()

    def __str__(self):
        return self.name
    