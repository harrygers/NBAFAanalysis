def main():
	bigMen = [ 
	["LeBron James", .59, 9.1, 8.6, 3, 4.2, 80, 33, 82],
	["Kevin Durant", .586, 5.4, 6.8, 2.9, 3, 82, 30, 68],
	["Giannis Antetokounmpo", .545, 4.8, 10, 3.6, 3, 83, 24, 75],
	["Anthony Davis", .552, 2.3, 11.1, 4.9, 2.2, 80, 25, 75],
	["Joel Embiid", .514, 3.2, 11, 3.8, 3.7, 84, 24, 63],
	["Nikola Jokic", .554, 6.1, 10.7, 2.9, 2.8, 82, 23, 75],
	["Draymond Green", .516, 7.3, 7.6, 5.4, 2.9, 79, 28, 28],
	["Karl-Anthony Towns", .596, 2.4, 12.3, 3.4, 1.9, 84, 23, 82],
	["Rudy Gobert", .622, 1.4, 10.7, 5, 1.9, 85, 26, 56],
	["Kevin Love", .552, 1.7, 9.3, 1.6, 1.5, 82, 30, 59],
	["LaMarcus Albridge", .52, 2, 8.5, 3.5, 1.5, 83, 33, 75],
	["Blake Griffin", .493, 5.8, 7.4, 1.8, 2.8, 82, 29, 58],
	["Al Horford", .553, 4.7, 7.4, 3.8, 1.8, 82, 32, 72],
	["Clint Capela", .652, .9, 10.8, 4.1, 1.4, 82, 24, 74],
	["Aaron Gordon", .5, 2.3, 7.9, 2, 1.8, 81, 23, 58],
	["Andre Drummond", .529, 3, 16, 5.7, 2.6, 83, 25, 78],
	["Steven Adams", .629, 1.2, 9, 3, 1.7, 84, 25, 76],
	["Myles Turner", .523, 1.3, 6.4, 2.5, 1.5, 83, 22, 65],
	["Marc Gasol", .473, 4.2, 8.1, 2.6, 2.7, 85, 34, 73],
	["Kristaps Porzingis", .489, 1.2, 6.6, 2, 1.9, 87, 22, 48]
	]

	smallMen = [
	["Steph Curry", .618, 6.1, 5.1, 1.8, 3, 75, 30, 51],
	["James Harden", .541, 8.8, 5.4, 3.8, 4.4, 77, 29, 72],
	["Russell Westbrook", .477, 10.3, 10.1, 4.5, 4.8, 72, 30, 80],
	["Kawhi Leonard", .539, 2.3, 4.7, 5.5, 1.8, 79, 27, 9],
	["Damian Lillard", .519, 6.6, 4.5, 2.7, 2.8, 75, 28, 73],
	["Chris Paul", .55, 7.9, 5.4, 2.7, 2.2, 72, 33, 58],
	["Paul George", .521, 3.3, 5.7, 3.9, 2.7, 81, 28, 79],
	["Jimmy Butler", .512, 4.9, 5.3, 2.8, 1.8, 80, 29, 59],
	["Victor Oladipo", .537, 4.3, 5.2, 4, 2.9, 76, 26, 75],
	["Ben Simmons", .545, 8.2, 8.1, 5, 3.4, 82, 22, 81],
	["Klay Thompson", .585, 2.5, 3.8, 1.8, 1.8, 79, 28, 73],
	["Kyrie Irving", .568, 5.1, 3.8, 2.7, 2.3, 75, 26, 60],
	["Kyle Lowry", .553, 6.9, 5.6, 3.1, 2.3, 73, 32, 78],
	["Donovan Mitchell", .506, 3.7, 3.7, 3.8, 2.7, 75, 22, 79],
	["Jayson Tatum", .538, 1.6, 5, 4, 1.4, 80, 20, 80],
	["Jrue Holiday", .543, 6, 4.5, 2.9, 2.6, 76, 28, 81],
	["Kemba Walker", .516, 5.6, 3.1, 2, 2.2, 73, 28, 80],
	["Bradley Beal", .527, 4.5, 4.4, 2.5, 2.6, 77, 25, 82],
	["CJ McCollum", .506, 3.4, 4, 2.9, 1.9, 75, 27, 81],
	["Devin Booker", .501, 4.7, 4.5, .6, 3.6, 78, 22, 54],
	["John Wall", .466, 9.6, 3.7, 1.5, 3.9, 76, 28, 41],
	["Khris Middleton", .524, 4, 5.2, 2.3, 2.3, 80, 27, 82],
	["Jaylen Brown", .54, 1.6, 4.9, 3.2, 1.8, 79, 22, 70],
	["Otto Porter Jr", .581, 2, 6.4, 3.1, 1, 80, 25, 77],
	["DeMar DeRozan", .488, 5.2, 3.9, 2.8, 2.2, 79, 29, 80],
	["Gordon Hayward", .536, 3.5, 5.4, 3.3, 1.9, 80, 28, 73],
	["Eric Gordon", .54, 2.2, 2.5, 1.8, 1.9, 76, 29, 69],
	["Gary Harris", .57, 2.9, 2.6, 1.5, 1.8, 76, 24, 67],
	["Mike Conley", .475, 5.6, 2.9, 2, 1.8, 73, 31, 12],
	["Jamal Murray", .529, 3.4, 3.7, 1.2, 2.1, 76, 21, 81]
	]

	print("This program ranks NBA players for free agency, it is divided by big men and small men.")
	position = input("Type big or small for respective rankings")
	if position == "big":
		bigEval(bigMen)
	elif position == "small":
		smallEval(smallMen)
	else:
		print("Please type big or small.")

def bigEval(players):
	#Paul & Beitz Matrix Value Weights
	eFieldGoal = .23
	assists = .05
	rebounds = .18
	dws = .19
	turnOvers = .08
	height = .1
	age = .12
	gamesPlayed = .05
	#Below is the code that indexs and weights each players individual stats
	index = 0
	tempPBval = 0
	for i in range(len(players)):
		eFieldGoalVal = players[i][1] * eFieldGoal
		assistsVal =  players[i][2] * assists
		reboundsVal = players[i][3] * rebounds
		dwsVal = players[i][4] * dws
		turnOversVal = players[i][5] * turnOvers
		heightVal = players[i][6] * height
		ageVal = (33 - players[i][7]) * age
		gamesPlayedVal = players[i][8] * gamesPlayed
		totalPB = eFieldGoalVal + assistsVal + reboundsVal + dwsVal + turnOversVal + heightVal + ageVal + gamesPlayedVal
		print(players[i][0])
		print(totalPB)
		if totalPB > tempPBval:
			index = i
			tempPBval = totalPB
	#player with the highest PB score
	print()
	print("The big player with the highest rating is: ", players[index][0])



def smallEval(players):
	#Paul & Beitz Matrix Value Weights
	eFieldGoal = .3
	assists = .2
	rebounds = .07
	dws = .11
	turnOvers = .09
	height = .06
	age = .12
	gamesPlayed = .05
	#Below is the code that indexs and weights each players individual stats
	index = 0
	tempPBval = 0
	for i in range(len(players)):
		eFieldGoalVal = players[i][1] * eFieldGoal
		assistsVal =  players[i][2] * assists
		reboundsVal = players[i][3] * rebounds
		dwsVal = players[i][4] * dws
		turnOversVal = players[i][5] * turnOvers
		heightVal = players[i][6] * height
		ageVal = (33 - players[i][7]) * age
		gamesPlayedVal = players[i][8] * gamesPlayed
		totalPB = eFieldGoalVal + assistsVal + reboundsVal + dwsVal + turnOversVal + heightVal + ageVal + gamesPlayedVal
		print(players[i][0])
		print(totalPB)
		if totalPB > tempPBval:
			index = i
			tempPBval = totalPB
	#player with the highest PB score
	print()
	print("The small player with the highest rating is: ", players[index][0])

main()
