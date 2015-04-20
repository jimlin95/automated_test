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
def enable_device_admin_setting(vc, name):
    setting = vc.findViewWithTextOrRaise(name).getParent()
    if not setting.children[len(setting.children) - 1].isChecked():
        print(name + " not enabled...enabling")
        setting.touch()
        vc.dump()
        vc.findViewById("com.android.settings:id/action_button").touch()
        vc.dump()
    else:
        print(name + " enabled")

def set_device_admins(vc):
        package = 'com.android.settings'
        activity = '.DeviceAdminSettings'
        component_name = package + '/' + activity
        vc.device.startActivity(component=component_name)
        vc.dump()
        enable_device_admin_setting(vc,"android.deviceadmin.cts.CtsDeviceAdminReceiver")
        enable_device_admin_setting(vc,"android.deviceadmin.cts.CtsDeviceAdminReceiver2")

if __name__ == '__main__':
    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device=device, serialno=serialno)
    # Press the HOME button to start the test from the home screen
    device.press('KEYCODE_HOME','DOWN_AND_UP')
    set_device_admins(vc)
    # Press the HOME button to start the test from the home screen
    device.press('KEYCODE_HOME','DOWN_AND_UP')
