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
from com.dtmilano.android.viewclient import ViewClient, View, UiDevice 
from cts_develop import ChangeDeveloper_settings
from cts_setsecurity import setSecurity
from cts_settimezone import setTimezone
from cts_wifisetting import SetWifiConnect,ModifyNetwork
from cts_skipwizzard import skip_setupwizzard
from cts_setchrome import set_chrome


os.system("adb devices")
# Connect to device with the IP received as a parameter
device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device=device, serialno=serialno)
ud = UiDevice(vc=vc)
vc.sleep(1)
print u'Start to Skip setup wizzard'
skip_setupwizzard(vc)
print u'Skip setup wizzard --- Done'
# Press the HOME button to start the test from the home screen
device.press('KEYCODE_HOME','DOWN_AND_UP')

#Change language to English (United States)
print u'Start to Change Language to English'
ud.changeLanguage('en-rUS')
print u'Change Language to English --- Done'
print u'Start to Change the settings in Developer'
ChangeDeveloper_settings(vc)
print u'Change the settings in Developer --- Done'
print u'Start to Change the settings in Security'
setSecurity(vc)
print u'Change the settings in Security --- Done'
print u'Start to Change the TimeZone to GMT + 00:00'
setTimezone(vc)
print u'Change the TimeZone to GMT + 00:00 --- Done'
print u'Start to Connect device to Wifi'
SetWifiConnect(vc,u'dlink-549',u'38017549')
print u'Connect device to Wifi --- Done'
print u'Start to Modify the network to fit CTS\'s requirement'
ModifyNetwork(vc,u'dlink-549')
print u'Modify the network to fit CTS\'s requirement --- Done'
# Press the HOME button to start the test from the home screen
device.press('KEYCODE_HOME','DOWN_AND_UP')
print u'Start to Run Chrome browser & confirm the settings'
set_chrome(vc)
print u'Run Chrome browser & confirm the settings --- Done'
device.press('KEYCODE_HOME','DOWN_AND_UP')

