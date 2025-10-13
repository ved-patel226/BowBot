from time import sleep_us
from machine import Pin

STEP = Pin(21, Pin.OUT)

STEPS_PER_REV = (
    200  # set to your motor's steps per revolution (adjust for microstepping)
)
DELAY_US = 1000  # pulse high/low time in microseconds (smaller = faster)

try:
    for _ in range(STEPS_PER_REV):
        STEP.on()
        sleep_us(DELAY_US)
        STEP.off()
        sleep_us(DELAY_US)

finally:
    STEP.off()
    print("Rotation complete")
