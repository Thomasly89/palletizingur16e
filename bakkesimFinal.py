from Python.robodk.robodk import *
from Python.robolink.robolink import *

#from Python.robodk.robodk import Mat

sim = Robolink()

robot = sim.Item("UR16e")
tool = sim.Item("gripperStorbox-v3201119")
pickFrame = sim.Item("Pickframe")
placeFrame1 = sim.Item("Placeframe1")
home = sim.Item("Home")
bakke = sim.Item("storbox-v2")
robotFram = sim.Item("UR16e Base")
wait1Frame = sim.Item("wait1")
heis = sim.Item("Heis")
heightFrame = sim.Item("Target 1")
placeFrame2 = sim.Item("placeFrame2")
wait1Frame2 = sim.Item("wait2")

wait2 = Mat(wait1Frame2.Pose())
height = Mat(heightFrame.Pose())
wait1 = Mat(wait1Frame.Pose())
pickTarget = Mat(pickFrame.Pose()*roty(pi)*rotz(pi/2))
placeTarget1 = Mat(placeFrame1.Pose()*roty(pi)*rotz(pi/2))
placeTarget2 = Mat(placeFrame2.Pose()*roty(pi)*rotz(-pi/2))

xPose = range(0,1000,530)
yPose = range(0,500,390)
zPose = range(0,-600,-120)

for z in zPose:
    for y in yPose:
        for x in xPose:
            bakke.Copy()
            new_bakke = sim.Paste(pickFrame)
            new_bakke.setPose(pickTarget * rotx(-pi) * rotz(-pi / 2) * transl(790, 130, -400))
            heis.MoveL(height)
            robot.MoveJ(home)
            robot.MoveL(pickTarget)
            tool.AttachClosest()
            robot.MoveJ(wait1*transl(0,0,z))
            robot.MoveL(placeTarget1*transl(x,y,z))
            tool.DetachAll()
            robot.MoveJ(home)


zPose1 = range(-400,-1100,-120)

for z1 in zPose1:
    for y in yPose:
        for x in xPose:
            bakke.Copy()
            new_bakke = sim.Paste(pickFrame)
            new_bakke.setPose(pickTarget * rotx(-pi) * rotz(-pi / 2) * transl(790, 130, -400))
            heis.MoveL(height)
            robot.MoveJ(home)
            robot.MoveL(pickTarget)
            tool.AttachClosest()
            heis.MoveJ(height*transl (0,0,650))
            robot.MoveJ(wait1*transl(0,0,z1+400))
            robot.MoveL(placeTarget1*transl(x,y,z1+450))
            tool.DetachAll()
            robot.MoveJ(home)

xPose1 = range(0,-1000,-530)
yPose1 = range(0,500,390)

for z in zPose:
    for y1 in yPose1:
        for x1 in xPose1:
            bakke.Copy()
            new_bakke = sim.Paste(pickFrame)
            new_bakke.setPose(pickTarget * rotx(-pi) * rotz(-pi / 2) * transl(790, 130, -400))
            heis.MoveL(height)
            robot.MoveJ(home)
            robot.MoveL(pickTarget)
            tool.AttachClosest()
            robot.MoveJ(wait2*transl(0,0,z))
            robot.MoveL(placeTarget2*transl(x1,y1,z))
            tool.DetachAll()
            robot.MoveJ(home)


for z1 in zPose1:
    for y1 in yPose1:
        for x1 in xPose1:
            bakke.Copy()
            new_bakke = sim.Paste(pickFrame)
            new_bakke.setPose(pickTarget * rotx(-pi) * rotz(-pi / 2) * transl(790, 130, -400))
            heis.MoveL(height)
            robot.MoveJ(home)
            robot.MoveL(pickTarget)
            tool.AttachClosest()
            heis.MoveJ(height*transl (0,0,650))
            robot.MoveJ(wait2*transl(0,0,z1+400))
            robot.MoveL(placeTarget2*transl(x1,y1,z1+450))
            tool.DetachAll()
            robot.MoveJ(home)