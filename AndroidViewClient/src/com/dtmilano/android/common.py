# -*- coding: utf-8 -*-
'''
Copyright (C) 2012-2015  Diego Torres Milano
Created on Jan 5, 2015

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

@author: Diego Torres Milano
'''
import platform
import os

def _nd(name):
    '''
    @return: Returns a named decimal regex
    '''
    return '(?P<%s>\d+)' % name

def _nh(name):
    '''
    @return: Returns a named hex regex
    '''
    return '(?P<%s>[0-9a-f]+)' % name

def _ns(name, greedy=False):
    '''
    NOTICE: this is using a non-greedy (or minimal) regex

    @type name: str
    @param name: the name used to tag the expression
    @type greedy: bool
    @param greedy: Whether the regex is greedy or not

    @return: Returns a named string regex (only non-whitespace characters allowed)
    '''
    return '(?P<%s>\S+%s)' % (name, '' if greedy else '?')

def obtainPxPy(m):
    px = int(m.group('px'))
    py = int(m.group('py'))
    return (px, py)

def obtainVxVy(m):
    wvx = int(m.group('vx'))
    wvy = int(m.group('vy'))
    return wvx, wvy

def obtainVwVh(m):
    (wvx, wvy) = obtainVxVy(m)
    wvx1 = int(m.group('vx1'))
    wvy1 = int(m.group('vy1'))
    return (wvx1-wvx, wvy1-wvy)

def obtainAdbPath():
    '''
    Obtains the ADB path attempting know locations for different OSs
    '''

    osName = platform.system()
    isWindows = False
    if osName.startswith('Windows'):
        adb = 'adb.exe'
        isWindows = True
    else:
        adb = 'adb'

    ANDROID_HOME = os.environ['ANDROID_HOME'] if os.environ.has_key('ANDROID_HOME') else '/opt/android-sdk'
    HOME = os.environ['HOME'] if os.environ.has_key('HOME') else ''

    possibleChoices = [ os.path.join(ANDROID_HOME, 'platform-tools', adb),
                       os.path.join(HOME,  "android", 'platform-tools', adb),
                       os.path.join(HOME,  "android-sdk", 'platform-tools', adb),
                       ]

    if osName.startswith('Windows'):
        possibleChoices.append(os.path.join("""C:\Program Files\Android\android-sdk\platform-tools""", adb))
        possibleChoices.append(os.path.join("""C:\Program Files (x86)\Android\android-sdk\platform-tools""", adb))
    elif osName.startswith('Linux'):
        possibleChoices.append(os.path.join("opt", "android-sdk-linux",  'platform-tools', adb))
        possibleChoices.append(os.path.join(HOME,  "opt", "android-sdk-linux",  'platform-tools', adb))
        possibleChoices.append(os.path.join(HOME,  "android-sdk-linux",  'platform-tools', adb))
        possibleChoices.append(os.path.join(HOME,  'Android', 'Sdk', 'platform-tools', adb))
    elif osName.startswith('Mac'):
        possibleChoices.append(os.path.join("opt", "android-sdk-mac_x86",  'platform-tools', adb))
        possibleChoices.append(os.path.join(HOME,  "opt", "android-sdk-mac", 'platform-tools', adb))
        possibleChoices.append(os.path.join(HOME,  "android-sdk-mac", 'platform-tools', adb))
        possibleChoices.append(os.path.join(HOME,  "opt", "android-sdk-mac_x86",  'platform-tools', adb))
        possibleChoices.append(os.path.join(HOME,  "android-sdk-mac_x86",  'platform-tools', adb))
    else:
        # Unsupported OS
        pass

    possibleChoices.append(adb)
    
    for exeFile in possibleChoices:
        if os.access(exeFile, os.X_OK):
            return exeFile

    for path in os.environ["PATH"].split(os.pathsep):
        exeFile = os.path.join(path, adb)
        if exeFile != None and os.access(exeFile, os.X_OK if not isWindows else os.F_OK):
            return exeFile

    raise Exception('adb="%s" is not executable. Did you forget to set ANDROID_HOME in the environment?' % adb)
