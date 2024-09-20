# gfons@raspberrypi:~ $ sudo pip3 install bluedot
# error: externally-managed-environment
# ...
# hint: See PEP 668 for the detailed specification.

gfons@raspberrypi:~ $ python3 -m venv .venv
gfons@raspberrypi:~ $ source .venv/bin/activate
(.venv) gfons@raspberrypi:~ $ 


(.venv) gfons@raspberrypi:~ $ pip3 install --upgrade pip setuptools wheel
...
      Successfully uninstalled pip-23.0.1
Successfully installed pip-24.2 setuptools-74.0.0 wheel-0.44.0
(.venv) gfons@raspberrypi:~ $ pip3 --version
pip 24.2 from /home/gfons/.venv/lib/python3.11/site-packages/pip (python 3.11)

(.venv) gfons@raspberrypi:~ $ pip3 install bluedot
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting bluedot
  Downloading https://www.piwheels.org/simple/bluedot/bluedot-2.0.0-py3-none-any.whl (37 kB)
Installing collected packages: bluedot
Successfully installed bluedot-2.0.0



# (.venv) gfons@raspberrypi:~ $ python3 Documents/2025-1_LAB_FSE/practica03/clase01.py 
# Traceback (most recent call last):
#   File "/home/gfons/Documents/2025-1_LAB_FSE/practica03/clase01.py", line 2, in <module>
#     from bluedot import BlueDot 
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   ...
#   File "/home/gfons/.venv/lib/python3.11/site-packages/bluedot/utils.py", line 3, in <module>
#     import dbus
# ModuleNotFoundError: No module named 'dbus'

# (.venv) root@raspberrypi:/home/gfons# pip3 install dbus-python
# Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
# Collecting dbus-python
#   Using cached dbus-python-1.3.2.tar.gz (605 kB)
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Preparing metadata (pyproject.toml) ... error
#   ...
#       ../subprojects/dbus-gmain/meson.build:107:11: ERROR: Dependency "dbus-1" not found, tried pkgconfig

gfons@raspberrypi:~ $ sudo apt install libdbus-1-dev libdbus-glib-1-dev
...
The following additional packages will be installed:
  libblkid-dev libdbus-glib-1-dev-bin libffi-dev libglib2.0-dev libglib2.0-dev-bin libmount-dev libpcre2-32-0
  libpcre2-dev libpcre2-posix3 libselinux1-dev libsepol-dev uuid-dev
...

(.venv) gfons@raspberrypi:~ $ pip3 install dbus-python
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
...
Successfully installed dbus-python-1.3.2

# Captura de make discoverable en raspi os

# ***********************************
# CLASE 1
# ***********************************
(.venv) gfons@raspberrypi:~ $ python3 Documents/2025-1_LAB_FSE/practica03/clase01.py 
Server started B8:27:EB:44:A5:C7
Waiting for connection

# Captura de blue dot en android

Client connected 18:4E:16:40:FA:AB
Hola Mundo
Hasta pronto

# ***********************************
# EXTRAS
# ***********************************

(.venv) gfons@raspberrypi:~ $ pip3 install gpiozero
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting gpiozero
  Downloading https://www.piwheels.org/simple/gpiozero/gpiozero-2.0.1-py3-none-any.whl (150 kB)
Collecting colorzero (from gpiozero)
  Downloading https://www.piwheels.org/simple/colorzero/colorzero-2.0-py2.py3-none-any.whl (26 kB)
Requirement already satisfied: setuptools in ./.venv/lib/python3.11/site-packages (from colorzero->gpiozero) (74.0.0)
Installing collected packages: colorzero, gpiozero
Successfully installed colorzero-2.0 gpiozero-2.0.1

(.venv) gfons@raspberrypi:~ $ pip3 install gpiozero rpi-gpio
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: gpiozero in ./.venv/lib/python3.11/site-packages (2.0.1)
Collecting rpi-gpio
  Downloading RPi.GPIO-0.7.1.tar.gz (29 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: colorzero in ./.venv/lib/python3.11/site-packages (from gpiozero) (2.0)
Requirement already satisfied: setuptools in ./.venv/lib/python3.11/site-packages (from colorzero->gpiozero) (74.0.0)
Building wheels for collected packages: rpi-gpio
  Building wheel for rpi-gpio (setup.py) ... done
  Created wheel for rpi-gpio: filename=RPi.GPIO-0.7.1-cp311-cp311-linux_aarch64.whl size=69910 sha256=8b6637776af73866e655fae5df46830c06b7c7514074b7755c302e5e51dc078e
  Stored in directory: /home/gfons/.cache/pip/wheels/58/9a/da/bc92ced3a63320f51bfb2eb461f0408a206acdcedfa57fbfbe
Successfully built rpi-gpio
Installing collected packages: rpi-gpio
Successfully installed rpi-gpio-0.7.1


# ***********************************
# ROOT
# ***********************************
pip3 show bluedot
pip3 show dbus-python


