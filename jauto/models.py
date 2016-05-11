from django.db import models
import datetime
from jasset.models import Asset, AssetGroup
from juser.models import User, UserGroup

# Create your models here.


class Application(models.Model):
    app_name = models.CharField(max_length=50)
    if_del = models.CharField(max_length=4)
    script_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.app_name


class Install(models.Model):
    host_id = models.CharField(max_length=30)
    host_name_show = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    host_name_show = models.CharField(max_length=30)
    app_name = models.CharField(max_length=50)
    script_location = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    apply_time = models.CharField(max_length=30)
    token = models.CharField(max_length=40)
    # def __unicode__(self):
    #     return self.app_name

