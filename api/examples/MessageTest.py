#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #   
 # @File UserTest.py
 # @Brief 
 # @Author abelzhu, abelzhu@tencent.com
 # @Version 1.0
 # @Date 2018-02-24
 #
 #
 
import sys
sys.path.append("D:/Python/weworkapi_python/api/src")

import random

from CorpApi import *
from TestConf import * 

## test
api = CorpApi(TestConf['CORP_ID'], TestConf['APP_SECRET'])

try :
##
    response = api.httpCall(
            CORP_API_TYPE['MESSAGE_SEND'],
            {
                "touser": "penghaifeng",
                "agentid": 1000015,
                'msgtype' : 'text',
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'text' : {
                    'content':'Hello,方法论',
                },
                'safe' : 0,
            })
    print (response) 
except ApiException as e :
    print (e.errCode, e.errMsg)

