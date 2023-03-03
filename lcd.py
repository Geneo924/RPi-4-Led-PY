#!/usr/bin/python3

from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

def s_exit(signum, frame):
	exit(1)

signal(SIGTERM, s_exit)
signal(SIGHUP, s_exit)

try:
	lcd.text("test test",1)
	lcd.text("line 2 test",2)

	pause()

except KeyboardInterrupt:
	pass

finally:
	lcd.clear()
