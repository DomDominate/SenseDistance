from time import sleep 
from gpiozero import DistanceSensor, PWMLED
from signal import signal, SIGTERM, SIGHUP, pause

led = PWMLED(13)
sensor = DistanceSensor(echo = 17, trigger = 4)

def terminate():
    exit(1)

signal(SIGTERM, terminate)
signal(SIGHUP, terminate)
led.on()
while True:
    distance = sensor.value
    print("distance:")
    print(distance)
    intensity = round (1.0 - distance, 1)
    print("LED intensity:")
    print(intensity)
    if intensity < 0:
        intensity = 0.0
    led.value = intensity
    sleep(0.1)



        
            

            
    