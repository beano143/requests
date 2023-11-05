import time 
import random 

def reminder(time):
  print(f"Drink your watter, it has been {time} since you were last told to ")

def random_time():
  randint = random.randint(10, 3600)
  time.sleep(randint)
  return randint

while True:
  time = random_time()
  reminder(time)
