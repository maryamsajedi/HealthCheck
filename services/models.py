from django.db import models

class Service(models.Model):
    url   = models.URLField(max_length=250)
    port  = models.CharField(max_length=50)
    name  = models.CharField(max_length=50, unique = True)
    status_code       = models.IntegerField()
    health_treshold   = models.IntegerField()
    unhealth_treshold = models.IntegerField()

    def __str__(self):
        return self.name
    