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

#from com.android.monkeyrunner import ViewClient, MonkeyDevice, MonkeyView
def accept_device_admin_install(vc):
    vc.dump()
    vc.findViewById("com.android.vending:id/positive_button").touch()

if __name__ == '__main__':
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device=device, serialno=serialno)
    # Press the HOME button to start the test from the home screen
    accept_device_admin_install(vc)
    # Press the HOME button to start the test from the home screen
