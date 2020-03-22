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

chatid = "test210";
try :
##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_CREATE'],
            {
                'name' : 'appchat_test',
                'owner' : 'penghaifeng',
                'userlist' : ['penghf', 'shanli', 'penghaifeng', ],
                'chatid' : chatid,
            })
    print (response) 
    chatid = response['chatid']
except ApiException as e :
    print (e.errCode, e.errMsg)

try :
    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_UPDATE'],
            {
                'chatid' : chatid,
                'name' : 'appchat_test_new_name',
                'owner' : 'shanli',
                'add_user_list' : ['penghaifeng', 'penghf']
            })
    print (response) 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_UPDATE'],
            {
                'chatid' : chatid,
                'name' : '应用发消息测试',
                'owner' : 'penghaifeng',
                'del_user_list' : 'penghf',
            })
    print (response) 

    ##
    #response = api.httpCall(
    #        CORP_API_TYPE['APP_CHAT_SEND'],
    #        {
    #            'chatid':chatid,
    #            'msgtype' : 'text',
    #            'text' : {'content':'我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党我是文本消息热爱祖国热爱人民热爱中国共产党'},
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
    #            'safe' : 1,
    #        })
    #print (response) 

    ##
    #response = api.httpCall(
    #        CORP_API_TYPE['APP_CHAT_SEND'],
    #        {
    #            'chatid':chatid,
    #            'msgtype' : 'image',
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
    #            'image' : {
    #                'media_id':'3lpbB2Z89bBmqYRVMIcpPF7zl1h-V-6oCZRxT3ewRzPQ',
    #            },
    #            'safe' : 1,
    #        })
    #print (response) 

    ##
    #response = api.httpCall(
    #        CORP_API_TYPE['APP_CHAT_SEND'],
    #        {
    #            'chatid':chatid,
    #            'msgtype' : 'file',
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
    #            'file' : {
    #                'media_id':'363LmmkUIEYosxmHDp8AZyC485ii7EFEdIFAHYnjy1s4',
    #            },
    #            'safe' : 1,
    #        })
    #print (response) 


    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'msgtype' : 'voice',
                'voice' : {
                    'media_id':'3VIIMc7QzZJqEGxJ8ALwnevPGFksjX0SSV7IhYl0H7YI',
                },
                'safe' : 1,
            })
    print (response) 

    ##
    #response = api.httpCall(
    #        CORP_API_TYPE['APP_CHAT_SEND'],
    #        {
    #            'chatid':chatid,
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
    #            'msgtype' : 'video',
    #            'video' : {
    #                'media_id':'3jtU3eCcZUpa_aSUGmOUH4PL46ENkQLkdDFU3TL7xgcy2gsKhGl4y4ojwhZX1h8B3',
    #            },
    #            'safe' : 1,
    #        })
    #print (response) 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'msgtype' : 'news',
		"news" : {
		    "articles" : [
			{
			    "title" : "图文消息",
			    "description" : "今年中秋节公司有豪礼相送",
			    "url" : "https://work.weixin.qq.com/",
			    "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
			    "btntxt":"更多",
			},
			{
			    "title" : "图文消息",
			    "description" : "今年中秋节公司有豪礼相送",
			    "url" : "https://work.weixin.qq.com/",
			    "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
			    "btntxt":"更多",
			},
			{
			    "title" : "图文消息",
			    "description" : "今年中秋节公司有豪礼相送",
			    "url" : "https://work.weixin.qq.com/",
			    "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
			    "btntxt":"更多",
			},
                    ]
            },
            'safe' : 0, 
            }, 
            )
    print (response) 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                'msgtype' : 'textcard',
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'textcard' : {
                    'title':'我是文本卡片消息',
                    'description' : 'aaaaaaa',
                    'url' : 'www.qq.com',
                    'btntxt' : '更多',
                },
                'safe' : 1,
            })
    print (response) 

    ##
    response = api.httpCall(
            CORP_API_TYPE['APP_CHAT_SEND'],
            {
                'chatid':chatid,
                "msgtype" : "mpnews",
                "mpnews": { 
                    "articles" : [
                        { 
                            "title" : "图文消息(mpnews)",
                            "thumb_media_id" : "3lpbB2Z89bBmqYRVMIcpPF7zl1h-V-6oCZRxT3ewRzPQ",
                            "author" : "author",
                            "content" : "content",
                            "digest" : "我是图文"
                        },
                        { 
                            "title" : "图文消息(mpnews)",
                            "thumb_media_id" : "3lpbB2Z89bBmqYRVMIcpPF7zl1h-V-6oCZRxT3ewRzPQ",
                            "author" : "author",
                            "content" : "content",
                            "digest" : "我是图文"
                        },
                        { 
                            "title" : "图文消息(mpnews)",
                            "thumb_media_id" : "3lpbB2Z89bBmqYRVMIcpPF7zl1h-V-6oCZRxT3ewRzPQ",
                            "author" : "author",
                            "content" : "content",
                            "digest" : "我是图文"
                        },
                    ]
                },
    #           'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'safe' : 1,
            })
    print (response) 

except ApiException as e :
    print (e.errCode, e.errMsg)
