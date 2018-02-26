#!/bin/bash

#kodi-send –action=”Notification(SYNC,Resilio Sync wird gestartet auf USB,3000)”
cd /opt/resilio/bin
sudo ./rslsync --webui.listen 0.0.0.0:8888

