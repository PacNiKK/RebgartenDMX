import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel):
    print(channel)
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 3 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(3,GPIO.RISING,callback=button_callback) # Setup event on pin 3 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up