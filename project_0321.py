#Magician
import time
pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]
if True:
	if True:
		if True:
			decision = "LOSS"
			if True:
				if decision == "HIT":
					dType.SetPTPCmd(api, 1, x, y, -70, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, -40, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, -70, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, z, rHead, 1)
				if decision == "STAND":
					dType.SetPTPCmd(api, 1, x+10, y+80, z, rHead, 0)
					dType.SetPTPCmd(api, 1, x-10, y-80, z, rHead, 0)
					dType.SetPTPCmd(api, 1, x, y, z, rHead, 0)
				if decision == "WIN":
					dType.SetPTPCmd(api, 1, x, y, z+100, rHead, isQueued=0)
					dType.SetPTPCmd(api, 1, x, y, z+50, rHead, isQueued=0)
					dType.SetPTPCmd(api, 1, x, y, z+100, rHead, isQueued=0)
					dType.SetPTPCmd(api, 1, x, y, z, rHead, isQueued=0)
				if decision == "LOSS":
					dType.SetPTPCmd(api, 1, x, y, z, rHead, isQueued=1)
					dType.SetPTPCmd(api, 1, x+70, y, z, rHead, isQueued=1)
					dType.SetPTPCmd(api, 1, x+80, y+20, z, rHead, isQueued=1)
					time.sleep(0.5)
					dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
					time.sleep(0.5)
					dType.SetPTPCmd(api, 2, x+80, y+20, -71, rHead, isQueued=1)
					dType.SetPTPCmd(api, 2, x+80, y+20, z+100, rHead, isQueued=1)
					dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
					dType.SetPTPCmd(api, 1, x, y, z, rHead, isQueued=1)
				if decision == "PUSH":
					l = 1
					while l <= 2:
						dType.SetPTPCmd(api, 1, x+20, y-20, z+10, rHead, isQueued=0)
						dType.SetPTPCmd(api, 1, x+20, y-20, z-10, rHead, isQueued=0)
						dType.SetPTPCmd(api, 1, x-20, y+20, z+10, rHead, isQueued=0)
						dType.SetPTPCmd(api, 1, x-20, y+20, z-10, rHead, isQueued=0)
						l+=1
					dType.SetPTPCmd(api, 1, x, y, z, rHead, isQueued=0)