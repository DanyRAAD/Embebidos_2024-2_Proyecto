#!/bin/bash

# Instalar pip para Python 3
sudo apt-get install python3-pip

# Instalar librerías pyudev y python-vlc
pip3 install pyudev python-vlc

# Instalar VLC y udisks2
sudo apt-get install vlc udisks2

# Actualizar el sistema
sudo apt-get update
sudo apt-get upgrade

# Instalar o actualizar Widevine
sudo apt install libwidevinecdm0 -y

# Actualizar completamente el sistema
sudo apt update
sudo apt full-upgrade -y

# Instalar xinit y Chromium Browser
sudo apt-get install xinit chromium-browser
