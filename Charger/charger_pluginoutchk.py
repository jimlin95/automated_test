#! /usr/bin/env python                                                                                                                                                                                                                                                                                                                                                                                                
# -*- coding: utf-8 -*-
#Copyright (C) 2015-2016 Quanta Computer, Inc.
#Date : 2015/04/21                                             
#Description : The function is simulation USB plug-in & out uevent update.
#Return : -1 Fail, 0 Success
#Author : Edison lee                                           
#Project : For UZ1                                             

import sys
import os

# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if p not in sys.path:
            sys.path.append(p)
except:
   pass

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass
try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'examples'))
except:
    pass
# This must be imported before AndroidViewClient,
# otherwise the import fails.
try:
    from com.dtmilano.android.viewclient import ViewClient, View
except:
    pass

#~~~~~~~~~~~~~~~~~~~ Variable ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
package_battery='com.android.settings'
activity_battery='.fuelgauge.PowerUsageSummary'
component_battery=package_battery + "/" + activity_battery
home_key=u'KEYCODE_HOME'
charge_charging=u'Charging (USB)'
charge_not_charging=u'Not charging'
charge_full_charging=u'Full'
status='false'
sus_vbus_cmd='adb shell "echo 1 > /sys/class/power_supply/smb347-usb/suspend_vbus_supply"'
nonsus_vbus_cmd='adb shell "echo 0 > /sys/class/power_supply/smb347-usb/suspend_vbus_supply"'

#~~~~~~~~~~~~~~~~~~~ Function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def SimSourceInOut(device,vc):
    global status
    device.startActivity(component=component_battery)
    ViewClient.sleep(3)
    vc.dump()
    no_id7 = vc.findViewByIdOrRaise("id/no_id/7")
    print('Simulation USB Plug-in...')
    temp_in = vc.findViewByIdOrRaise("android:id/title").getText().split('-')
    for x in temp_in:
        if x.find(charge_charging) != -1:
            print('Okay, charging...')
            status = 'true'
	elif x.find(charge_full_charging) != -1:
	    print('Okay, Full so not charging...')
            status = 'true'
    if status != 'true':
        print('Fail, not charging...')
        return -1
    print('Simulation USB Plug-out...')
    os.system(sus_vbus_cmd)
    ViewClient.sleep(3)
    vc.dump()
    temp_out = vc.findViewByIdOrRaise("android:id/title").getText().split('-')
    for x in temp_out:
        if x.find(charge_not_charging) != -1:
            print('Okay, Not charging...')
            status = 'true'
    if status != 'true':
        print('Fail, charging...')
        return -1
    ViewClient.sleep(3)
    os.system(nonsus_vbus_cmd)
    print("END")
#~~~~~~~~~~~~~~~~~~~~~ Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
     # Connect to device with the IP received as a parameter
	device, serialno = ViewClient.connectToDeviceOrExit()
        vc = ViewClient(device=device, serialno=serialno)
	device.press(home_key)
	if SimSourceInOut(device,vc) != -1:
	    print("Auto test success")
	    exit(0)
	else:
	    print("Auto test fail")
	    exit(1)
