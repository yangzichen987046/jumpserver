#!/usr/bin/env python
#coding:utf-8

import datetime
from django import template

register = template.Library()

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        #返回的是格式化后的时间表示字符串
        return now.strftime(self.format_string)

    @register.tag(name="current_time")
    def do_current_time(parser, token):
        try:
            tag_name, format_string = token.split_contents()
        except ValueError:
            msg = '%r tag requires a single argument' % token.split_contents()[0]
            raise template.TemplateSyntaxError(msg)
        return CurrentTimeNode(format_string[1:-1])

