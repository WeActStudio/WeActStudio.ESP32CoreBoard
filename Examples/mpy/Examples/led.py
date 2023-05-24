#  - WeAct Studio Official Link
#  - taobao: weactstudio.taobao.com
#  - aliexpress: weactstudio.aliexpress.com
#  - github: github.com/WeActStudio
#  - gitee: gitee.com/WeAct-TC
#  - blog: www.weact-tc.cn

import machine
import esp

machine.freq(240000000)
print('ESP32 Core Board Designed By WeAct Studio')
print('CPU Freq.: ' + str(machine.freq()/1000000) + 'Mhz')
print('Flash Size: ' + str(esp.flash_size()/1024) + 'kB')

from utime import sleep,ticks_ms
from machine import Pin, PWM

print('led with smooth duty change Example')

DUTY_MAX = 2**16 - 1

duty_u16 = 0
delta_d = 48

p = PWM(Pin(22), 2000, duty_u16=duty_u16)
print(p)

tick = 0
led_tick = 0
while True:
    tick = ticks_ms()
    
    if tick >= led_tick:
        led_tick = tick + 1
        
        p.duty_u16(duty_u16)

        duty_u16 += delta_d
        if duty_u16 >= DUTY_MAX:
            duty_u16 = DUTY_MAX
            delta_d = -delta_d
        elif duty_u16 <= 0:
            duty_u16 = 0
            delta_d = -delta_d
