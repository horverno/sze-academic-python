from sense_hat import SenseHat # vagy import sense_hat as sh és akkor SenseHat() helyett pl sh.SenseHat()
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

sense.show_letter("S", red)
sleep(1)
sense.show_letter("Z", blue)
sleep(1)
sense.show_letter("E", green)
sleep(1)
sense.show_letter("E", white)
sleep(1)
sense.show_letter(".", red)
sleep(1)
sense.clear()
