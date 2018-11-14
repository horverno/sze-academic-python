import sense_hat as sh
#import matplotlib.pyplot as plt
import time

sense = sh.SenseHat()
sense.set_imu_config(False, True, True)  # gyro + accel
sense.show_message("Joystick>>stop:", text_colour=[200, 40, 20], scroll_speed=0.05)

run = True
while run:
    orientation = sense.get_orientation()
    print("%5.1f" % (orientation["yaw"]))
    time.sleep(0.2)
    if sense.stick.get_events() != []:
        run = False

