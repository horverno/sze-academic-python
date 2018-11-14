import sense_hat as sh
import matplotlib.pyplot as plt
import time
import random
import math

sense = sh.SenseHat()
sense.set_imu_config(False, True, True)  # gyro + accel
#sense.show_message("Joystick>>stop:", text_colour=[200, 40, 20], scroll_speed=0.05)

run = True
while run:
    if sense.stick.get_events() != []:
        run = False
    orientation = sense.get_orientation()
    print("%5.1f" % (orientation["yaw"]))
    yaw = orientation["yaw"]
    time.sleep(0.2)
    x = math.sin(math.radians(yaw))
    y = math.cos(math.radians(yaw))
    plt.ylim([-1, 1])
    plt.xlim([-1, 1])
    plt.plot([x, 0], [y, 0], "*-")
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

plt.show()

