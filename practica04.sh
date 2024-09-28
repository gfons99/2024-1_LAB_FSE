sudo apt-get update && sudo apt-get upgrade -y  
sudo apt-get install python-setuptools  
sudo apt-get install python-pip  
sudo pip install pyTelegramBotAPI  
sudo apt-get install sysstat  
sudo chown -R pi:pi /home/pi/pyTelegramApi  
cd /home/pi/pyTelegramBotApi  
sudo python setup.py install  


# ********************************
# 1
# ********************************
gfons@raspberrypi:/ $ sudo apt-get update && sudo apt-get upgrade -y

# ********************************
# 2
# ********************************
gfons@raspberrypi:/ $ sudo apt-get install python3-setuptools 
...
python3-setuptools is already the newest version (66.1.1-1).
...

# ********************************
# 3
# ********************************
gfons@raspberrypi:/ $ sudo apt-get install python3-pip  
...
python3-pip is already the newest version (23.0.1+dfsg-1+rpt1).
...

# ********************************
# 4
# ********************************
gfons@raspberrypi:/ $ python3 -m venv .venv
gfons@raspberrypi:/ $ source .venv/bin/activate
(.venv) gfons@raspberrypi:/ $ pip3 install pyTelegramBotAPI 
...
Successfully installed certifi-2024.8.30 charset-normalizer-3.3.2 idna-3.10 pyTelegramBotAPI-4.23.0 requests-2.32.3 urllib3-2.2.3

# ********************************
# 5
# ********************************
gfons@raspberrypi:/ $ sudo apt-get install sysstat
...
sysstat is already the newest version (12.6.1-1).
...

# ********************************
# 6
# ********************************
gfons@raspberrypi:/ $ mkdir /home/gfons/pyTelegramApi