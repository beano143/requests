from pynput.keyboard import Key, Controller
import time 
import os

keybpard = conytrolletr()

def get_time_local(time_zone):
  os.environ['TZ'] = time_zone
  time.tzset()
  val  = time.strftime('%X')
  val = val.split(":")
  
  if int(val[0]) >= 12:
    val[0] = int(val[0]) - 12
    val[0] = str(val[0])
    
  val1 = val[1].split("0")
  
  if val1[0] == "0":
    val1 = val1[1]
    
  return f"{val[0]}:{val1}" # retuns time in standard form

def return_time(time):
  keyboard.press('y')
  keyboard.release('y')

  kyboard.type(f"{time}")

  keyboard.press(enter)
  keyboadr.release(enter) # simulates all the key presses to input time 

while True:
  time_local = get_time_local('EST+05EDT,M4.1.0,M10.5.0')
  return_time(time_local)
  time.sleep(30)
