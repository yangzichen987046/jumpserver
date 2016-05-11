# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.db.models import Q
from django.contrib.sessions.models import Session

from juser.user_api import *
from jnginx.models import *
import time


# @require_role(role='super')
def rec_assess_log(request):
    """
    封装方法，提供API以写入访问日志
    """
    token = request.GET.get('token', '')
    ip = request.GET.get('ip', '')
    province = request.GET.get('province', '')
    access_time = request.GET.get('access_time', '')
    api = request.GET.get('api', '')
    response_time = request.GET.get('response_time', '')

    access_time = time.mktime(time.strptime(access_time, '%d/%b/%Y:%H:%M:%S'))
    site_info = Site.objects.all().get(token=token)
    access_log_insert = Access_Log(
        site_id=site_info.id,
        ip=ip,
        access_time=access_time,
        province=province,
        api=api,
        response_time=response_time,
        access_status=0
    )
    access_log_insert.save()
    return HttpResponse(0)


# @require_role(role='super')
def cal_access_num(request):
    site_id = request.GET.get('site_id', '')

    time_str = time.time()
    time_str = time.localtime(time_str)
    time_str = time.strftime("%d/%b/%Y:%H:%M",time_str)
    time_str += ':00'
    str_time = time.mktime(time.strptime(time_str, '%d/%b/%Y:%H:%M:%S'))
    time_start = float(str_time) - 5*60
    time_end = float(str_time) - 1

    province_list = Province.objects.all()
    for province in province_list:
        records_num = Access_Log.objects.filter(site_id=site_id).filter(access_time__gte=time_start).filter(access_time__lte=time_end).filter(province=province).count()
        if records_num > 0:
            minute_log = Minute_Log(
                site_id=site_id,
                province=province,
                access_num=records_num,
                time=str_time
            )
            minute_log.save()
    return HttpResponse(0)