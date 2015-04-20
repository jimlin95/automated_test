#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os

# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if not p in sys.path:
            sys.path.append(p)
except:
   pass

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

# This must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails.
from com.dtmilano.android.viewclient import ViewClient, View

def enable_developer_setting(vc, name):
    setting = vc.findViewWithTextOrRaise(name).getParent()
    if not setting.children[len(setting.children) - 1].isChecked():
        print(name + " not enabled...enabling")
        setting.touch()
    else:
        print(name + " enabled")
        
def ChangeDeveloper_settings(vc):
    package = 'com.android.settings'
    activity = '.DevelopmentSettings'
    component_name = package + '/' + activity
    vc.device.startActivity(component=component_name)
    vc.dump(-1)
    enable_developer_setting(vc,u'Stay awake')
   #enable_developer_setting(vc,u'USB debugging')
    enable_developer_setting(vc,u'Allow mock locations')

if __name__ == '__main__':
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device=device, serialno=serialno)
    # Press the HOME button to start the test from the home screen
    device.press('KEYCODE_HOME','DOWN_AND_UP')
    ChangeDeveloper_settings(vc) 
    # Press the HOME button to start the test from the home screen
    device.press('KEYCODE_HOME','DOWN_AND_UP')
