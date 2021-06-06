#!/bin/bash

PASSWORD=$1

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pyinstaller --onefile main.py
echo $PASSWORD | sudo -S cp -r dist/main /bin/Hello_Smoke
