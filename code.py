import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


echo = 2 ## echo  pin for ultrasonic sensor
trig = 3 ## trigger pin for ultrasonic sensor
led = 13 ## led pin

threshold = 150

GPIO.setup(led, GPIO.OUT) # sets led pin as output
pwm = GPIO.PWM(led, threshold)

GPIO.setup(trig, GPIO.OUT)# sets led pin as output
GPIO.setup(echo, GPIO.IN)# sets led pin as output

pwm.start(0)

time.sleep(2)

def Distance():
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while (GPIO.input(echo) == 0):
        start_t = time.time()
    while (GPIO.input(echo) == 1):
        end_t = time.time()

    t = end_t - start_t
    dist = t(34000/2)
    return dist

val1 = Distance()
pwm.ChangeDutyCycle(100 - (val2))
print(" Distance:", val, "cm")
try:
    while True:
        val2 = Distance()
        if (val2 >= 400):
            print("Object out of range limit")
        elif (val2 > 80):
            pwm.ChangeDutyCycle(0)
    else:
        pwm.ChangeDutyCycle(100 - (val1*2))
        print("Distance:", val1, "cm")

    time.sleep(1)
except:
    print(" error ")
finally:
    GPIO.cleanup()
