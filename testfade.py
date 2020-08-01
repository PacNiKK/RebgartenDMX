from gpiozero import LED, Button
from signal import pause
button=Button(3)
button.when_pressed=print("Button was pressed")
pause()