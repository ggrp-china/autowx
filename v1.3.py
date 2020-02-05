#--coding:utf-8 --
'''
*Created on 2020-1-30  
*Author:ggrp
*Version 1.3
*Title: 微信的自动接龙
'''

import itchat,_thread,time,re,random,datetime


itchat.auto_login(hotReload=True)
itchat.send("已登录！",toUserName='filehelper')

with open('tomorrow.txt') as fp:
    a = fp.read()

today = str(datetime.date.today())[-2:]

if today != a:
    itchat.send("没到，退出！",toUserName='filehelper')
    exit()


login =True
def keep_run(app):
    global login
    assert(login==True)
    app.run()
    login = False

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    global a
    global today
    if "健康" in msg['Text'] and a == today:
        result = re.findall("[0-9]{1}", msg['Text'])
        if len(result)>0:
            tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))[-2:]
            with open('tomorrow.txt','w') as fp:
                fp.write(tomorrow)
            a = tomorrow
            return msg['Text'] +"\n"+str(int(result[-1])+1)+ '.xx xx 健康 '

_thread.start_new_thread(keep_run,(itchat,))

begin = time.time()
while 1:
    time.sleep(1)
    end = time.time()
    if end - begin >= 300:
        itchat.send("无情况，退出！",toUserName='filehelper')
        exit()
