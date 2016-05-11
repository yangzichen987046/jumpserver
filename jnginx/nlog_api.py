# coding: utf-8
from __future__ import division
import xlrd
import xlsxwriter
from django.db.models import AutoField
from jumpserver.api import *
from jasset.models import ASSET_STATUS, ASSET_TYPE, ASSET_ENV, IDC, AssetRecord, Assetgroup_Usergroup, Asset_Group, Region
from jperm.ansible_api import MyRunner
from jperm.perm_api import gen_resource
from jumpserver.templatetags.mytags import get_disk_info
from juser.models import AccessKey, User_Group
from juser.key_api import auto_add_host, get_assetgroupid_by_usergroupid
from jauto.models import *
from jnginx.models import *
import commands
import hashlib
import json


def get_all_location():
    location = {}
    province_all = Province.objects.all()
    for province in province_all:
        location[province.province] = [province.location]
    site_all = Site.objects.all()
    for site in site_all:
        location[site.site_name] = [site.location]
    return location
