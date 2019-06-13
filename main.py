import time

import gpiozero

import drivetrain

drivetrain = drivetrain.Drivetrain([gpiozero.Motor(22, 27, 17)], [gpiozero.Motor(3, 2, 4)])

while True:
   drivetrain.setBothOutputs(1, 1)
   time.sleep(2)
   drivetrain.setBothOutputs(-1, -1)
   time.sleep(2)
