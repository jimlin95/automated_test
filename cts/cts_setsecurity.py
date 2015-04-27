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
from common import  findid_and_touch, findtext_and_touch
def setSecurity(vc):
        package = 'com.android.settings'
        activity = '.SecuritySettings'
        component_name = package + '/' + activity
        vc.device.startActivity(component=component_name)
        vc.dump()
        ret = findtext_and_touch(vc,u'Screen lock')
        if ret == 0:
            return 0
        ret = findtext_and_touch(vc,u'None')
        if ret == 0:
            return 0
        return 1

if __name__ == '__main__':
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device=device, serialno=serialno)
    # Press the HOME button to start the test from the home screen
    device.press('KEYCODE_HOME','DOWN_AND_UP')
    setSecurity(vc)
    # Press the HOME button to start the test from the home screen
    device.press('KEYCODE_HOME','DOWN_AND_UP')
