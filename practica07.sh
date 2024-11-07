gfons@raspberrypi:~ $ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.137.26  netmask 255.255.255.0  broadcast 192.168.137.255
        inet6 fe80::434a:ef55:f4c3:3312  prefixlen 64  scopeid 0x20<link>
        ...

gfons@raspberrypi:~ $ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.106  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 2806:106e:24:16f9::5  prefixlen 128  scopeid 0x0<global>
        ...

gfons@raspberrypi:~ $ iwconfig
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=31 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on


gfons@raspberrypi:~ $ nmcli -f WIFI-PROPERTIES.AP device show wlan0
WIFI-PROPERTIES.AP:                     yes


gfons@raspberrypi:~ $ sudo nmcli d wifi hotspot ifname wlan0 ssid raspberry-unam password pass1234
Device 'wlan0' successfully activated with 'e72ca09e-148b-47ab-a4ec-71c07fc26691'.
Hint: "nmcli dev wifi show-password" shows the Wi-Fi name and password.

gfons@raspberrypi:~ $ nmcli con show
NAME                            UUID                                  TYPE       DEVICE 
Hotspot                         e72ca09e-148b-47ab-a4ec-71c07fc26691  wifi       wlan0  
Wired connection 1              fb4e5605-6bac-3604-9f67-e79c863723fe  ethernet   eth0   
lo                              7805f19a-59af-49de-a327-e49cf3f8858c  loopback   lo     
