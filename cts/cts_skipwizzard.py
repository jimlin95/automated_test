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

def skip_setupwizzard(vc):
    # page 1
    ret = findid_and_touch(vc,'com.google.android.setupwizard:id/start')
    if ret == 0:
        return 0
    # page 2 (wifi)
    ret = findid_and_touch(vc,'com.android.settings:id/custom_button')
    if ret == 0:
        return 0

    # page 2 sub page (wifi)
    ret = findid_and_touch(vc,'android:id/button2')
    if ret == 0:
        return 0
    # page 3
    ret = findid_and_touch(vc,'com.google.android.setupwizard:id/next_button')
    if ret == 0:
        return 0
    # page 4
    ret = findid_and_touch(vc,'com.google.android.setupwizard:id/next_button')
    if ret == 0:
        return 0
    # page 5
    ret = findid_and_touch(vc,'com.google.android.setupwizard:id/next_button')
    if ret == 0:
        return 0
    ret = findtext_and_touch(vc,'OK')
    if ret == 0:
        return 0
    ret = findtext_and_touch(vc,'OK')
    if ret == 0:
        return 0


if __name__ == '__main__':
    os.system("adb devices")
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device=device, serialno=serialno)
    skip_setupwizzard(vc) 
