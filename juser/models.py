# coding: utf-8

from django.db import models
from django.contrib.auth.models import AbstractUser
import time
# from jasset.models import Asset, AssetGroup


class UserGroup(models.Model):
    name = models.CharField(max_length=80, unique=True)
    comment = models.CharField(max_length=160, blank=True, null=True)

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('SU', 'SuperUser'),
        ('GA', 'GroupAdmin'),
        ('CU', 'CommonUser'),
    )
    name = models.CharField(max_length=80)
    uuid = models.CharField(max_length=100)
    role = models.CharField(max_length=2, choices=USER_ROLE_CHOICES, default='CU')
    group = models.ManyToManyField(UserGroup)
    ssh_key_pwd = models.CharField(max_length=200)
    # is_active = models.BooleanField(default=True)
    # last_login = models.DateTimeField(null=True)
    # date_joined = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.username


class AdminGroup(models.Model):
    """
    under the user control group
    用户可以管理的用户组，或组的管理员是该用户
    """

    user = models.ForeignKey(User)
    group = models.ForeignKey(UserGroup)

    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.group.name)


class Document(models.Model):
    def upload_to(self, filename):
        return 'upload/'+str(self.user.id)+time.strftime('/%Y/%m/%d/', time.localtime())+filename

    docfile = models.FileField(upload_to=upload_to)
    user = models.ForeignKey(User)


class AccessKey(models.Model):
    key_id = models.CharField(max_length=100)
    key_secret = models.CharField(max_length=100)
    # group_id = models.CharField(max_length=80)
    # user_id = models.CharField(max_length=80)
    plat_id = models.CharField(max_length=80)
    if_del = models.CharField(max_length=80)
    add_time = models.CharField(max_length=80)

    # user = models.ForeignKey(User)

    group = models.ForeignKey(UserGroup)

    def __unicode__(self):
        return '%s: %s: %s: %s: %s: %s: %s: %s: %s: %s' % (self.id, self.key_id,
                                                           self.key_secret, self.group_id,
                                                           self.user_id, self.plat_id,
                                                           self.if_del, self.add_time,
                                                           self.group.name)


class User_Group(models.Model):
    user = models.ForeignKey(User)
    usergroup = models.ForeignKey(UserGroup)

