#Magician
import time
prev_state = 0
state = -1
pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]
while True:
	with open(r"C:\Users\tagu.ti6a493\Documents\GitHub\MustJaak\decision.txt") as f:
		rida = f.read()
		if rida != "":
			decision = rida.strip().split()
			decision, state= decision
			state = int(state)
			if state != prev_state:
				if decision == "HIT":
					dType.SetPTPCmd(api, 1, x, y, -70, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, -40, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, -70, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, z, rHead, 1)
				if decision == "STAND":
					dType.SetPTPCmd(api, 1, x-20, y+80, z, rHead, 0)
					dType.SetPTPCmd(api, 1, x-20, y-80, z, rHead, 0)
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
				time.sleep(4)
				prev_state = state
