from time import sleep_us
from machine import Pin
import math

STEP = Pin(21, Pin.OUT)

STEPS_PER_REV = 200  # set to your motor's steps per revolution
REVOLUTIONS = 10

# Delay bounds (microseconds). Higher = slower, lower = faster.
DELAY_MIN_US = 300
DELAY_MAX_US = 1500

total_steps = max(2, STEPS_PER_REV * REVOLUTIONS)
delta = DELAY_MAX_US - DELAY_MIN_US
two_pi = 2 * math.pi

try:
    for i in range(total_steps * 2):
        t = i / (total_steps - 1)
        s = 0.5 - 0.5 * math.cos(two_pi * t)
        delay = int(DELAY_MAX_US - s * delta)

        STEP.on()
        sleep_us(delay)
        STEP.off()
        sleep_us(delay)

finally:
    STEP.off()
    print("Rotation complete")
