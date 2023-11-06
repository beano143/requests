from pynput.keyboard import Key, Controller
import time 
import os

keybpard = conytrolletr()

def get_time_local():
  os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
  time.tzset()
  val  = time.strftime('%X')
  val = val.split(":")
  
  if int(val[0]) >= 12:
    val[0] = int(val[0]) - 12
    val[0] = str(val[0])
    
  val1 = val[1].split("0")
  
  if val1[0] == "0":
    val1 = val1[1]
    
  return f"{val[0]}:{val1}"

def return_time(time):
  keyboard.press('y')
  keyboard.release('y')

  kyboard.type(f"{time})

  keyboard.press(enter)
  keyboadr.release(enter)

while True:
  get_time_local()
  return_time()
  time.sleep(10)
