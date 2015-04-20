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
def findandtouch(vc,string):
	elem = 	vc.findViewWithText(string)
	if elem:
        	elem.touch()
		vc.dump()

def setTimezone(vc):        
        package = 'com.android.settings'
        activity = '.Settings'
        component_name = package + '/' + activity
        vc.device.startActivity(component=component_name)
        vc.dump()
        view = None
        android___id_list = vc.findViewByIdOrRaise("android:id/list")       
        android___id_list.uiScrollable.setViewClient(vc)
        view = android___id_list.uiScrollable.scrollTextIntoView(u'Date & time')
        if view is not None:  
            view.touch()
        else:
            raise RuntimeError("Couldn't find Date & time") 
        vc.dump()
        findandtouch(vc,u'Select time zone')
        view = None
        android___id_list = vc.findViewByIdOrRaise("android:id/list")       
        android___id_list.uiScrollable.setViewClient(vc)
        android___id_list.uiScrollable.flingToBeginning(maxSwipes=6)
        vc.dump(-1)
        view = android___id_list.uiScrollable.scrollTextIntoView(u'London, Dublin')
        if view is not None:  
            view.touch()
        else:
            raise RuntimeError("Couldn't change timezone to GMT+00:00") 
 
if __name__ == '__main__':
        # Connect to device with the IP received as a parameter
        device, serialno = ViewClient.connectToDeviceOrExit()
        vc = ViewClient(device=device, serialno=serialno)
        device.press('KEYCODE_HOME','DOWN_AND_UP')

        setTimezone(vc)

        # Press the HOME button to start the test from the home screen
        device.press('KEYCODE_HOME','DOWN_AND_UP')
