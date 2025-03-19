#Magician
import time
prev_state = 0
prev_games = 0
state = 0
while True:
	with open(r"C:\Users\tagu.ti6a493\Documents\GitHub\MustJaak\decision.txt") as f:
		rida = f.read()
		if rida != "":
			decision = rida.strip().split()
			decision, state, new_games= decision
			state = int(state)
			if prev_games == 0:
				prev_games = new_games
			if state != prev_state or new_games != prev_games:
				if decision == "HIT":
					pos = dType.GetPose(api)
					x = pos[0]
					y = pos[1]
					z = pos[2]
					rHead = pos[3]
					dType.SetPTPCmd(api, 1, x, y, -70, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, -40, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, -70, rHead, 1)
					dType.SetPTPCmd(api, 1, x, y, z, rHead, 1)
				if decision == "STAND":
					pos = dType.GetPose(api)
					x = pos[0]
					y = pos[1]
					z = pos[2]
					rHead = pos[3]
					dType.SetPTPCmd(api, 1, x-20, y+80, z, rHead, 0)
					dType.SetPTPCmd(api, 1, x-20, y-80, z, rHead, 0)
					dType.SetPTPCmd(api, 1, x, y, z, rHead, 0)
				time.sleep(4)
				prev_state = state
				prev_games = new_games