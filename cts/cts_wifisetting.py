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
def SetWifiConnect(vc,ap_name,ap_password):
        package = 'com.android.settings'
        activity = '.Settings'
        component_name = package + '/' + activity
#        ap_name = "dlink-549"
#        ap_password = "38017549"
        # Open the Settings app
        vc.device.startActivity(component=component_name)
        # Enable Wi-Fi
        vc.device.shell("svc wifi enable")
        vc.dump()
        findtext_and_touch(vc,u'Wi‑Fi')        
        i = 0
        br_ap=vc.findViewWithText(ap_name)
        while not br_ap and i<30:
                br_ap=vc.findViewWithText(ap_name)
                ViewClient.sleep(1)
                vc.dump()
                i += 1
        if i == 30:
                print "Cannot enable Wi-Fi"
    
        br_ap.touch()
        vc.device.type(ap_password)
        vc.dump()
        findtext_and_touch(vc,u'Connect')
        vc.sleep(1)
def ModifyNetwork(vc,ap_name):
        package = 'com.android.settings'
        activity = '.Settings'
#        ap_name = u"dlink-549"
        component_name = package + '/' + activity
        # Open the Settings app
        vc.device.startActivity(component=component_name)
        vc.dump()
        findtext_and_touch(vc,u'Wi‑Fi')        
        #long press ap_name 
        wifi_ap = vc.findViewWithTextOrRaise(ap_name)      
        (x,y) = wifi_ap.getXY()
        wifi_ap.device.drag((x,y), (x,y), 2000, 1)
        vc.dump()
        findtext_and_touch(vc,u'Modify network')        
        findtext_and_touch(vc,u'Show advanced options')        

        findtext_and_touch(vc,u'DHCP')        

        findtext_and_touch(vc,u'Static')        
        vc.device.dragDip((200.0, 724.0), (214.67, 418.67), 1000, 20, 0)
        vc.dump()
        ret, dns1 = findid_and_touch(vc,'com.android.settings:id/dns1')
        guardrail = 0
        maxSize = len(dns1.text()) 
        while maxSize > guardrail:
            guardrail += 1
            vc.device.press('KEYCODE_DEL')
        vc.device.press('KEYCODE_ENTER')
        dns1.setText('8.8.4.4')
        vc.device.press('KEYCODE_ENTER')
        vc.dump()
        findtext_and_touch(vc,u'Save')

if __name__ == '__main__':
        # Connect to device with the IP received as a parameter
        device, serialno = ViewClient.connectToDeviceOrExit()
        vc = ViewClient(device=device, serialno=serialno)
        device.press('KEYCODE_HOME','DOWN_AND_UP')
        SetWifiConnect(vc,u'dlink-549',u'38017549')
        ModifyNetwork(vc,u'dlink-549')

        # Press the HOME button to start the test from the home screen
#        device.press('KEYCODE_HOME','DOWN_AND_UP')
