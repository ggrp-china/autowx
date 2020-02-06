# -*- encoding=utf8 -*-
'''
*Created on 2020-2-5
*Author:ggrp
*Version 4.0
*Title: 微信的自动接龙
因为3.0太无脑了加上配置繁杂，换了一种方式写


安卓模拟器：MUMU
AirtestIDE
'''
import re
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
while 1:
    touch((196,279),duration=0.1,times=2)

    try:
        a = poco("com.tencent.mm:id/aun").get_text()
        break
    except:
        pass

result = re.findall("[0-9]{1}",a)
a = (a+"\n" +str(int(result[-1])+1)+ '.xx xx 健康').split("\n")
touch((196,279),duration=0.1,times=2)
poco("com.tencent.mm:id/aol").click()
sleep(1.0)
for i in a:
    text(i.strip())

poco("com.tencent.mm:id/aot").click()



