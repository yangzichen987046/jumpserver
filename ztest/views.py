#coding:utf-8

def index(request):
    parameters = {}
    parameters['Action'] = 'DescribeRegions'
    parameters['Version'] = '2014-05-26'
    parameters['AccessKeyId'] = 'testid'
    parameters['TimeStamp'] = 'DescribeRegions'
    parameters['SignatureMethod'] = 'HMAC-SHA1'
    parameters['SignatureVersion'] = '1'
    parameters['SignatureNonce'] = '123'
    parameters['Format'] = 'XML'

    # sorted(parameters.iteritems(),value,reverse=False)

    return my_render('ztest/index.html', locals(), request)
    # return HttpResponse(1)