from pynput.keyboard import Key, Controller
import time 
import os

keybpard = conytrolletr()

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
  
print(f"{val[0]}:{val1})
