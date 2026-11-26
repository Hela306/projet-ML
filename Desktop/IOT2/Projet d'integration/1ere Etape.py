from machine import Pin
from dht import DHT22
from time import sleep

capteur = DHT22(Pin(23))

while True:
    try:
        capteur.measure()
        h = capteur.humidity()
        t = capteur.temperature()
        f = (t * 9 / 5) + 32

        print("Humidité    : {:.1f} %".format(h))
        print("Température : {:.1f} °C".format(t))
        print("Température : {:.1f} °F".format(f))
        print("------------------------")

    except OSError:
        print("Échec de réception du capteur DHT22")

    sleep(2)  # toujours attendre 2 s entre deux mesures