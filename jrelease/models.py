from django.db import models
import datetime
from jasset.models import Asset, AssetGroup,Asset_Group
from juser.models import User, UserGroup

# Create your models here.

class Project(models.Model):
    proj_name = models.CharField(max_length=30)
    release_host_name = models.CharField(max_length=30)
    release_host_ip = models.CharField(max_length=30)
    release_host_id = models.CharField(max_length=30)
    # release_host_id = models.ManyToManyField(Asset, related_name='host_id')
    cluster_id = models.CharField(max_length=30)
    cluster_name = models.CharField(max_length=30)
    if_del = models.CharField(max_length=4)
    add_time = models.CharField(max_length=15)
    usergroup_id = models.CharField(max_length=11)
    check_port = models.CharField(max_length=8)
    check_url = models.CharField(max_length=200)


class Cluster(models.Model):
    cluster_name = models.CharField(max_length=30)
    usergroup_id = models.CharField(max_length=11)
    if_del = models.CharField(max_length=4)
    hosts = models.CharField(max_length=50)
    add_time = models.CharField(max_length=20)


class Upload_Code(models.Model):
    usergroup_id = models.CharField(max_length=11)
    proj_id = models.CharField(max_length=11)
    proj_name = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    code_name = models.CharField(max_length=100)
    release_status = models.CharField(max_length=4)
    release_time = models.CharField(max_length=15)


class Detail(models.Model):
    code_version_id = models.CharField(max_length=11)
    host_id = models.CharField(max_length=30)
    host_ip = models.CharField(max_length=30)
    host_name_show = models.CharField(max_length=30)
    check_port = models.CharField(max_length=8)
    check_url = models.CharField(max_length=200)
    release_status = models.CharField(max_length=4)
    release_time = models.CharField(max_length=15)