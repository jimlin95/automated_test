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

def SetWifiConnect(vc):
        package = 'com.android.settings'
        activity = '.Settings'
        component_name = package + '/' + activity
        ap_name = "dlink-549"
        ap_password = "38017549"
        # Open the Settings app
        vc.device.startActivity(component=component_name)
        # Enable Wi-Fi
        vc.device.shell("svc wifi enable")
        vc.dump()
        wifi = vc.findViewWithTextOrRaise(u'Wi‑Fi')        
        if wifi:
                wifi.touch()
                vc.dump()
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
        connect = vc.findViewWithText(u'Connect')
        if connect:
                connect.touch()
                vc.sleep(3)
def ModifyNetwork(vc):
        package = 'com.android.settings'
        activity = '.Settings'
        ap_name = u"dlink-549"
        component_name = package + '/' + activity
        # Open the Settings app
        vc.device.startActivity(component=component_name)
        vc.dump()
        wifi = vc.findViewWithTextOrRaise(u'Wi‑Fi')        
        if wifi:
                wifi.touch()
                vc.dump()
        #long press ap_name 
        wifi_ap = vc.findViewWithTextOrRaise(ap_name)      
        (x,y) = wifi_ap.getXY()
        wifi_ap.device.drag((x,y), (x,y), 2000, 1)
        vc.dump(-1)
        modifynetwork = vc.findViewWithTextOrRaise(u'Modify network')        
        if modifynetwork:
            modifynetwork.touch()
            vc.dump()

        advance_options = vc.findViewWithTextOrRaise(u'Show advanced options')        
        if advance_options:
            advance_options.touch()
            vc.dump()

        ip_settings = vc.findViewWithTextOrRaise(u'DHCP')        
        if ip_settings:
            ip_settings.touch()
            vc.dump()

        static = vc.findViewWithTextOrRaise(u'Static')        
        if static:
            static.touch()
            vc.dump()
        vc.device.dragDip((200.0, 724.0), (214.67, 418.67), 1000, 20, 0)
        vc.dump()
        dns1 = vc.findViewById('com.android.settings:id/dns1')
        dns1.touch()
        guardrail = 0
        maxSize = len(dns1.text()) 
        while maxSize > guardrail:
            guardrail += 1
            vc.device.press('KEYCODE_DEL')
            #device.press('KEYCODE_FORWARD_DEL')
        vc.device.press('KEYCODE_ENTER')
        dns1.setText('8.8.4.4')
        vc.device.press('KEYCODE_ENTER')
        vc.dump(-1)
        save = vc.findViewWithTextOrRaise(u'Save')
        if save:
            save.touch()
            vc.dump()

if __name__ == '__main__':
        # Connect to device with the IP received as a parameter
        device, serialno = ViewClient.connectToDeviceOrExit()
        vc = ViewClient(device=device, serialno=serialno)
        device.press('KEYCODE_HOME','DOWN_AND_UP')
        SetWifiConnect(vc)
        ModifyNetwork(vc)

        # Press the HOME button to start the test from the home screen
#        device.press('KEYCODE_HOME','DOWN_AND_UP')
