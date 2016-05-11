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
import commands
import hashlib
from jrelease.models import *


def get_code_upload_dir():
    dir_name = os.path.join('/data/web', 'package')
    mkdir(dir_name, mode=0777)
    return dir_name


def get_code_ftp_dir():
    # dir_name = os.path.join('/data/web', 'package')
    # mkdir(dir_name, mode=0777)
    dir_name = os.path.join('/data/web')
    return dir_name


def db_add_upload_code(**kwargs):
    """
    add project to db
    上传代码时数据库操作函数
    """
    code = Upload_Code(**kwargs)
    code.save()

