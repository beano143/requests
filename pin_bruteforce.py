from pynput.keyboard import Key, Controller

keyboard = Controller()

for A in range(0,9):
  for B in range(0,9):
    for C in range(0,9):
      for D in range(0,9):
        pin = f"{A}{B}{C}{D}"
        keyboard.type(pin)
        keyboard.press(enter)
        keyboard.release(enter)
