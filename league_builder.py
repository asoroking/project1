# PROJECT 1
# Build a Soccer League

# logic and function calls inside of an if __name__ == "__main__": block

# if __name__ == "__main__":


import csv

# read the data from the supplied CSV file : soccer_players.csv
# return data in tuple 
def read_file():
    with open("soccer_players.csv") as csvfile:
		players = csv.DictReader(csvfile, delimiter = ',')	
		players = tuple(players)
		return(players)


def write_file(teamname, teammembers):
    with open("teams.txt", "a") as file:
		file.write(str(teamname)+"\n")
		
		for member in teammembers: 
			line = str(member['Name']) + ', ' + str(member['Soccer Experience']) + ', ' + str(member['Guardian Name(s)'])
			file.write(line + "\n")
		
		file.write("\n") # delimiter between teams


def write_teams_to_file(*teams):
	open('teams.txt', 'w').close() # clean the file
	for team in teams:
		for k,v in team.items():
			write_file(k, v) # pass teamname and teammembers list to write_file function


def experiance(players):
	experts = []
	nonexperts = []
	for one in players:
		if one['Soccer Experience'] == 'YES': 
			experts.append(one)
		else:
			nonexperts.append(one)
	return(experts, nonexperts)

	
def create_teams(all_players):
	good, soso = experiance(all_players) # sort players by experiance
	team1 = [] ; team2 = [] ; team3 = []
	
	#carousel :)
	c1 = 1 ; c2 = 2 ; c3 = 3 ; i = 0
	for one in good:
		i+=1
		if i == c1:	team1.append(one); c1+=3; continue
		if i == c2: team2.append(one); c2+=3; continue
		if i == c3: team3.append(one); c3+=3; continue
		
	c1 = 1 ; c2 = 2 ; c3 = 3 ; i = 0
	for one in soso:
		i+=1
		if i == c1: team1.append(one); c1+=3; continue
		if i == c2: team2.append(one); c2+=3; continue
		if i == c3: team3.append(one); c3+=3; continue		

	return(team1, team2, team3)

	
# read the list of signed up soccer players
PLAYERS = read_file()

# sort players and define three teams
Dragons, Sharks, Raptors = create_teams(PLAYERS)

# cretae list of teams and team's members
write_teams_to_file({'Dragons': Dragons}, {'Sharks' : Sharks}, {'Raptors' : Raptors})






