from time import sleep_us
from machine import Pin
import math

STEP = Pin(21, Pin.OUT)

STEPS_PER_REV = 200
REVOLUTIONS = 10

DELAY_MIN_US = 1000


try:
    total_steps = max(2, STEPS_PER_REV * REVOLUTIONS)

    for i in range(total_steps * 2):
        delay = DELAY_MIN_US

        STEP.on()
        sleep_us(delay)
        STEP.off()
        sleep_us(delay)

finally:
    STEP.off()
    print("Rotation complete")
