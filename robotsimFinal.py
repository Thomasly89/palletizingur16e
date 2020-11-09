from Python.robodk.robodk import *
from Python.robolink.robolink import *

sim = Robolink()

robot = sim.Item("UR16e")
tool = sim.Item("verktøyLitenBoxFirev2")
home = sim.Item("Home")
wait = sim.Item("wait1")
wait2 = sim.Item("wait2")
heis = sim.Item("Heis")
target1 = sim.Item("Target 3")
hight2 = sim.Item("Target 4")
hight3 = sim.Item("Target 5")

robot.MoveJ(home)

box = sim.Item("fireien")

robotFrame = sim.Item("UR16e Base")
pickFrame = sim.Item("pickFrame")
placeFrame1 = sim.Item("placeFrame")
placeFrame2 = sim.Item("placeFrame2")
pickTarget = Mat(pickFrame.Pose()*roty(pi)*rotz(pi/2))
placeTarget1 = Mat(placeFrame1.Pose()*roty(pi)*rotz(pi/2))
placeTarget2 = Mat(placeFrame2.Pose()*roty(pi)*rotz(-pi/2))
wait1 = Mat(wait.Pose())
wait3 = Mat(wait2.Pose())
hight1 = Mat(target1.Pose())


yPos = range(0,-541,-180)
xPose = range(0,1000,180)
zPose = range(0,-600,-100)




for z in zPose:
    for x in xPose:

        heis.MoveL(target1)
        box.Copy()
        new_box = sim.Paste(pickFrame)
        new_box.setPose(pickTarget*rotx(-pi)*rotz(-pi/2)*transl(650,-60,-500))
        robot.MoveJ(pickTarget * transl(0, 0, -300))
        robot.MoveL(pickTarget)
        tool.AttachClosest()
        robot.MoveJ(wait1 * transl(0, 0, z))
        robot.MoveL(placeTarget1* transl(x, 0, z ))
        tool.DetachAll()
        robot.MoveJ(home)

xPose1 = range(0,1000,180)
zPose1 = range(-600,-1300,-100)

for z1 in zPose1:

    for x1 in xPose1:
        box.Copy()
        new_box = sim.Paste(pickFrame)
        new_box.setPose(pickTarget * rotx(-pi) * rotz(-pi / 2) * transl(650, -60, -500))
        heis.MoveL(hight1)
        robot.MoveJ(pickTarget * transl(0, 0, -300))
        robot.MoveL(pickTarget)
        tool.AttachClosest()
        heis.MoveL(hight1 * transl(0,0,900))
        robot.MoveJ(wait1 * transl(0, 0, z1+300))
        robot.MoveL(placeTarget1 * transl(x1, 0, z1+450))
        tool.DetachAll()
        robot.MoveJ(home)
xPose1 = range(0,-1000, -180)

for z in zPose:
                for x2 in xPose1:
                    heis.MoveL(hight1)
                    box.Copy()
                    new_box = sim.Paste(pickFrame)
                    new_box.setPose(pickTarget*rotx(-pi)*rotz(-pi/2)*transl(650,-60,-500))
                    robot.MoveJ(pickTarget * transl(0, 0, -300))
                    robot.MoveL(pickTarget)
                    tool.AttachClosest()
                    robot.MoveJ(wait3 * transl(0, 0, z ))
                    #robot.MoveJ(wait2*transl(0,0,z+600))
                    robot.MoveL(placeTarget2* transl(x2, 0, z ))
                    tool.DetachAll()
                    robot.MoveJ(home)



for z1 in zPose1:

    for x2 in xPose1:
        box.Copy()
        new_box = sim.Paste(pickFrame)
        new_box.setPose(pickTarget * rotx(-pi) * rotz(-pi / 2) * transl(650, -60, -500))
        heis.MoveL(hight1)
        robot.MoveJ(pickTarget * transl(0, 0, -300))
        robot.MoveL(pickTarget)
        tool.AttachClosest()
        heis.MoveL(hight1 * transl(0,0,900))
        robot.MoveJ(wait3 * transl(0, 0, z1+300))
        robot.MoveL(placeTarget2 * transl(x2, 0, z1+450))
        tool.DetachAll()
        robot.MoveJ(home)