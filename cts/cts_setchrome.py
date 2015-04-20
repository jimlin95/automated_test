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

def set_chrome(vc):
    # page 1
    package = 'com.android.chrome'
    activity = 'com.google.android.apps.chrome.Main'
    component_name = package + '/' + activity
    vc.device.startActivity(component=component_name)
    vc.dump(-1)
    vc.findViewById('com.android.chrome:id/terms_accept').touch()
    vc.dump(-1)
    vc.findViewById('com.android.chrome:id/negative_button').touch()

if __name__ == '__main__':
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device=device, serialno=serialno)
    set_chrome(vc)
    device.press('KEYCODE_HOME','DOWN_AND_UP')
