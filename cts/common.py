#! /usr/bin/env python
# -*- coding: utf-8 -*-
def findid_and_touch(vc,id):
    for i in range(3):
        try:
            button = vc.findViewById(id)
            if button:
                button.touch()
                vc.dump()
                vc.sleep(1)
                return 1, button
            else:
                vc.sleep(2)
                vc.dump()
        except ValueError:
            vc.dump()
    print 'CAN NOT find the View id "%s"'  %id
    return 0, 0
def findtext_and_touch(vc,text):
    for i in range(3):
        try:
        	button = vc.findViewWithText(text)
	        if button:
	            button.touch()
	            vc.dump()
	            return 1, button
	        else:
	            vc.dump()

        except ValueError:
            vc.dump()
    print 'CAN NOT find the View Text "%s"' %text
    return 0, 0


