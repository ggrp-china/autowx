#--coding:utf-8 --
'''
*Created on 2020-1-30  
*Author:ggrp
*Version 3.0
*Title: 微信的自动接龙
web版微信限制太大且出现了凌晨会自动退出的问题，
转安卓模拟器实现，这是单纯用模拟按键+安卓模拟器实现的自动接龙很没有技术含量
模拟器:雷电模拟器4
'''
import pyautogui
import time
import pyperclip
import re
from pykeyboard import PyKeyboard
time.sleep(5)

while "健康" not in pyperclip.paste():
    pyautogui.keyDown('A')#在模拟器对应位置加个键盘点击，实现复制第一个接龙
    time.sleep(1)
    pyautogui.keyUp('A')
    time.sleep(1)
    pyautogui.keyDown('B')
    pyautogui.keyUp('B')
    time.sleep(1)
    

result = re.findall("[0-9]{1}",pyperclip.paste())
if len(result)>0:
    pyperclip.copy(pyperclip.paste()+"\n"
                   +str(int(result[-1])+1)
                   +'.xx xx 健康 ')#粘贴版增加，由于模拟器中粘贴版依旧是原来的所以在别的地方先复制再粘贴一遍
    pyautogui.moveTo(x=1500, y=500,duration=0.1,tween=pyautogui.linear)
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.moveTo(x=1209, y=1003,duration=0.1, tween=pyautogui.linear)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
