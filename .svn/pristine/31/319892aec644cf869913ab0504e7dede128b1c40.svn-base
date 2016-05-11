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


def db_add_install(**kwargs):
    """
    add a asset group in database
    数据库中添加待安装队列
    """
    install = Install(**kwargs)
    # install.token = make_token()
    install.save()


def make_token():
    """
    生成token
    """
    src1 = random.randint(1, 1000000)
    src1 = str(src1)
    m2 = hashlib.md5()
    m2.update(src1)
    src2 = src1 + 'live400.com'
    m2.update(src2)
    token = m2.hexdigest()
    return token


def send_key(ip, root_passwd):
    cmd = '/home/zsc/sendkey.sh {0} {1}'.format(ip, root_passwd)
    status,send_res = commands.getstatusoutput(cmd)
    return send_res


def sys_init(ip):
    cmd = 'ssh root@{0} /root/sys_init.sh'.format(ip)
    status,sys_init_res = commands.getstatusoutput(cmd)
    return sys_init_res


def modify_host_name(ip, new_name):
    cmd = 'ssh root@ip /tmp/shell/modify_hostname_new.sh new_name'.format(ip, new_name)
    status,modify_name_res = commands.getstatusoutput(cmd)
    return


