#!/usr/bin/python
import os
import xbmc
import xbmcgui
import xbmcaddon

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "start resilio sync"
xbmcgui.Dialog().ok(addonname, line1)
#os.system()
path = os.getcwd()[:-1]+"\\"
# call script resiliostart.sh
xbmc.executebuiltin("XBMC.RunScript("+path+"resiliostart.sh)")
