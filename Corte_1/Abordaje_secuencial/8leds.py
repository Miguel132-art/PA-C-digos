from machine import Pin
from time import sleep

# Lista de pines donde están conectados los LEDs
led_pins = [2, 4, 5, 18, 19, 21, 22, 23]

# Creamos lista de objetos LED
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Bucle principal
while True:
    for i in range(len(leds)):
        # Apagar el LED anterior (con índice circular)
        leds[i-1].value(0)   # cuando i=0 osea low led apagado, i-1 es el último LED
        
        # Encender el LED actual 1 led encendido
        leds[i].value(1)
        
        sleep(0.8) #tiempo de espera entre apagar el anterior led y encender el proximo led
