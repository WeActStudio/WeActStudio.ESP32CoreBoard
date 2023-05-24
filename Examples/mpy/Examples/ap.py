#  - WeAct Studio Official Link
#  - taobao: weactstudio.taobao.com
#  - aliexpress: weactstudio.aliexpress.com
#  - github: github.com/WeActStudio
#  - gitee: gitee.com/WeAct-TC
#  - blog: www.weact-tc.cn

from utime import sleep
sleep(0.5)
print('No IDE connect,start app now.')

import machine
import esp

machine.freq(240000000)
print('ESP32 Core Board Designed By WeAct Studio')
print('CPU Freq.: ' + str(machine.freq()/1000000) + 'Mhz')
print('Flash Size: ' + str(esp.flash_size()/1024) + 'kB')

import network
from machine import Pin
from utime import sleep,ticks_ms

print('AP Example')

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid='WeAct Studio') # set the SSID of the access point
ap.config(max_clients=1) # set how many clients can connect to the network
ap.active(True)         # activate the interface

print('LED GPIO22 Blink')

led = Pin(22, Pin.OUT)
key = Pin(0, Pin.IN)

tick = 0
led_tick = 0
key_tick = 0

key_value_old = 0
while True:
    tick = ticks_ms()
    
    if tick >= led_tick:
        led_tick = tick + 800
        
        if led.value() == 1:
            led.value(0)
        else:
            led.value(1)
            
    if tick >= key_tick:
        key_tick = tick + 20
        
        if key_value_old != key.value():
            if key.value() == 0:
                print('key 0 pressed')
                
            key_value_old = key.value()
            
            
        
