#!/usr/bin/env python3
#import evdev
from evdev import InputDevice, categorize, ecodes
from pyautogui import press, dragTo
gamepad = InputDevice('/dev/input/event4')

#button code variables (change to suit your device)
blue1 = 288 #a
blue2 = 289 #b
blue3 = 290 #c
blue4 = 291 #d
blue5 = 292 #e
red1  = 293 #f
red2  = 294 #g
red3  = 295 #h
red4  = 296 #i
red5  = 297 #j
but6  = 298 #k
but7  = 299 #l

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
  if event.type == ecodes.EV_KEY:
    if event.value == 1:
        dragTo(0, 0)
        dragTo(1, 1)
      if event.code == blue1:
        print("Blue Button 1 Pressed")
        press('a')
      elif event.code == blue2:
        print("Blue Button 2 Pressed")
        press('b')
      elif event.code == blue3:
        print("Blue Button 3 Pressed")
        press('c')
      elif event.code == blue4:
        print("Blue Button 4 Pressed")
        press('d')
      elif event.code == blue5:
        print("Blue Button 5 Pressed")
        press('e')
      elif event.code == red1:
        print("Red Button 1 Pressed")
        press('f')
      elif event.code == red2:
        print("Red Button 2 Pressed")
        press('g')
      elif event.code == red3:
        print("Red Button 3 Pressed")
        press('h')
      elif event.code == red4:
        print("Red Button 4 Pressed")
        press('i')
      elif event.code == red5:
        print("Red Button 5 Pressed")
        press('j')
      elif event.code == but6:
        print("Button 6 Pressed")
        press('k')
      elif event.code == but7:
        print("Button 7 Pressed")
        press('l')    
