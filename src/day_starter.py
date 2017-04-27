# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:24:10 2017

@author: Swapnil.Walke
"""
import sys
import os
import webbrowser
import datetime

"""Open All Applications Only When Laptop is Booted Up In Office Time"""
now = datetime.datetime.now()
if now.hour < 9 and now.hour > 18:
    sys.exit()

"""start outlook.exe"""
os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.exe")

"""start Jabber"""
os.startfile("C:\\Program Files (x86)\\Cisco Systems\\Cisco Jabber\\CiscoJabber.exe")

"""open chrome and necessary websites"""
chrome = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
chrome.open("https://jira.community.veritas.com/secure/Dashboard.jspa")
chrome.open("https://stash.veritas.com")
chrome.open("www.quora.com")