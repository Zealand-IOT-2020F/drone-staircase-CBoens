import Drone
import sys
import time

#here you should interact with the drone
print("booting")

drone1 = Drone.Drone('192.1.1.1',8889)

#Diagnostics

drone1.printinfo()

drone1.connect()

drone1.battery()

#Action

#ideen er at dronen letter, vender 180grader for at få højdemåleren tættere på trinet.
#flyver 5 gange 26 cm bagud drejer 90 grader mod uret, flyver 5 gange 29cm 

drone1.takeOff()

time.sleep(2)

drone1.cw(180)

time.sleep(2)

ymax1 = 0
ymax2 = 0
ymax3 = 0

while ymax1 < 128:
    drone1.stepUp(30, 26)
    time.sleep(5)
    ymax1 += 26

drone1.ccw(90)

while ymax2 < 145:
    drone1.stepUp(30, 29)
    time.sleep(5)
    ymax2 += 29

drone1.ccw(90)

while ymax3 < 128:
    drone1.stepUp(30, 26)
    time.sleep(5)
    ymax3 += 26




drone1.land()




drone1.battery()

drone1.ftime()