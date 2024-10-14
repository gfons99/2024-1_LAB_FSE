
# Seleccionamos las siguientes opciones

-> 3 Interface Options Configure connections to peripherals
...
-> I5  I2C Enable/disable automatic loading of I2C kernel module
...
Would you like the ARM I2C interface to be enabled?
-> <Yes>
...
The ARM I2C interface is enabled
-> <Ok>

######## changed
root@raspberrypi:/home/gfons# apt-get install i2c-tools python3-smbus
...
root@raspberrypi:/home/gfons# adduser gfons i2c
Adding user `gfons' to group `i2c' ...
Done.

######## SAME
gfons@raspberrypi:~ $ python3 -m venv .venv
gfons@raspberrypi:~ $ source .venv/bin/activate
(.venv) gfons@raspberrypi:~ $ pip3 install smbus2
...
