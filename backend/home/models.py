from django.conf import settings
from django.db import models
class Tappu(models.Model):
    'Generated Model'
    gadda = models.GenericIPAddressField(protocol="both",unpack_ipv4=True,)
