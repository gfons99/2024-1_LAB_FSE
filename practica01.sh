***********************************************
7
***********************************************
gfons@raspberrypi:~ $ sudo su
root@raspberrypi:/home/gfons# pinout
Description        : Raspberry Pi 3B+ rev 1.3
Revision           : a020d3
SoC                : BCM2837
RAM                : 1GB
Storage            : MicroSD
USB ports          : 4 (of which 0 USB3)
Ethernet ports     : 1 (300Mbps max. speed)
Wi-fi              : True
Bluetooth          : True
Camera ports (CSI) : 1
Display ports (DSI): 1

,--------------------------------.
| oooooooooooooooooooo J8 PoE +====
| 1ooooooooooooooooooo   12   | USB
|  Wi                    oo   +====
|  Fi  Pi Model 3B+ V1.3         |
| |D     ,---.           1o   +====
| |S     |SoC|            RUN | USB
| |I     `---'                +====
| |0               C|            |
|                  S|       +======
|                  I| |A|   |   Net
| pwr      |HDMI|  0| |u|   +======
`-| |------|    |-----|x|--------'

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

RUN:
POWER ENABLE (1)
         RUN (2)

POE:
TR01 TAP (1) (2) TR00 TAP
TR03 TAP (3) (4) TR02 TAP



For further information, please refer to https://pinout.xyz/



root@raspberrypi:/home/gfons# pwd
/home/gfons



root@raspberrypi:/home/gfons# mkdir
mkdir: missing operand
Try 'mkdir --help' for more information.
root@raspberrypi:/home/gfons# ls
Bookshelf  Documents  Music	Public	   Videos
Desktop    Downloads  Pictures	Templates
root@raspberrypi:/home/gfons# mkdir Temporal
root@raspberrypi:/home/gfons# ls
Bookshelf  Documents  Music	Public	   Temporal
Desktop    Downloads  Pictures	Templates  Videos



root@raspberrypi:/home/gfons# cat /proc/meminfo 
MemTotal:         929100 kB
MemFree:          281036 kB
MemAvailable:     525648 kB
Buffers:           19376 kB
Cached:           277704 kB
SwapCached:          964 kB
Active:           315160 kB
Inactive:         233432 kB
Active(anon):      91152 kB
Inactive(anon):   177208 kB
Active(file):     224008 kB
Inactive(file):    56224 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:        204796 kB
SwapFree:         203772 kB
Zswap:                 0 kB
Zswapped:              0 kB
Dirty:                28 kB
Writeback:             0 kB
AnonPages:        250568 kB
Mapped:           169476 kB
Shmem:             16832 kB
KReclaimable:      19124 kB
Slab:              47588 kB
SReclaimable:      19124 kB
SUnreclaim:        28464 kB
KernelStack:        4608 kB
PageTables:         7724 kB
SecPageTables:         0 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:      669344 kB
Committed_AS:    1660140 kB
VmallocTotal:   257687552 kB
VmallocUsed:       12736 kB
VmallocChunk:          0 kB
Percpu:              720 kB
CmaTotal:         262144 kB
CmaFree:          194896 kB



root@raspberrypi:/home/gfons# cat /proc/partitions
major minor  #blocks  name

   1        0       4096 ram0
   1        1       4096 ram1
   1        2       4096 ram2
   1        3       4096 ram3
   1        4       4096 ram4
   1        5       4096 ram5
   1        6       4096 ram6
   1        7       4096 ram7
   1        8       4096 ram8
   1        9       4096 ram9
   1       10       4096 ram10
   1       11       4096 ram11
   1       12       4096 ram12
   1       13       4096 ram13
   1       14       4096 ram14
   1       15       4096 ram15
 179        0   15603712 mmcblk0
 179        1     524288 mmcblk0p1
 179        2   15075328 mmcblk0p2



root@raspberrypi:/home/gfons# cat /proc/cpuinfo 
processor	: 0
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 1
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 2
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 3
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

Revision	: a020d3
Serial		: 0000000056ee0f6d
Model		: Raspberry Pi 3 Model B Plus Rev 1.3



root@raspberrypi:/home/gfons# cat /proc/version
Linux version 6.6.31+rpt-rpi-v8 (serge@raspberrypi.com) (gcc-12 (Debian 12.2.0-14) 12.2.0, GNU ld (GNU Binutils for Debian) 2.40) #1 SMP PREEMPT Debian 1:6.6.31-1+rpt1 (2024-05-29)



root@raspberrypi:/home/gfons# shutdown -r now



root@raspberrypi:/home/gfons# apt-get update
Hit:1 http://deb.debian.org/debian bookworm InRelease
Hit:2 http://deb.debian.org/debian-security bookworm-security InRelease
Hit:3 http://deb.debian.org/debian bookworm-updates InRelease
Hit:4 http://archive.raspberrypi.com/debian bookworm InRelease
Reading package lists... Done



root@raspberrypi:/home/gfons# apt-get upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  rpi-eeprom
1 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 35.4 MB of archives.
After this operation, 6,818 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://archive.raspberrypi.com/debian bookworm/main arm64 rpi-eeprom all 24.0-1 [35.4 MB]
Fetched 35.4 MB in 4s (7,894 kB/s)     
Reading changelogs... Done
(Reading database ... 128163 files and directories currently installed.)
Preparing to unpack .../rpi-eeprom_24.0-1_all.deb ...
Unpacking rpi-eeprom (24.0-1) over (23.2-1) ...
Setting up rpi-eeprom (24.0-1) ...
Processing triggers for man-db (2.11.2-2) ...



***********************************************
8
***********************************************
root@raspberrypi:/home/gfons# raspi-config

***********************************************
9
***********************************************
root@raspberrypi:/home/gfons# raspi-config
Created symlink /etc/systemd/system/multi-user.target.wants/vncserver-x11-serviced.service → /lib/systemd/system/vncserver-x11-serviced.service.

