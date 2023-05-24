# Installation instructions
Program your board using the esptool.py program, found here.

If you are putting MicroPython on your board for the first time then you should first erase the entire flash using:
```
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```

From then on program the firmware starting at address 0x1000:

```
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 xxxxx.bin
```