# PROJECT 1
# Build a Soccer League

# logic and function calls inside of an if __name__ == "__main__": block

if __name__ == "__main__":


	import csv
	import time

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
				compose_letter(teamname, member) # compose and send letter
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

		
	def compose_letter(teamname, member):
		# constructing the name of file
		name = list(member['Name'].lower())
		for n,i in enumerate(name):
			if i == ' ':
				name[n] = '_'	
		filename = str(''.join(name)) +".txt"
		with open(filename, "w") as file:
			file.write(   "Dear "
						+  str(member['Guardian Name(s)'])  + "," + "\n"*2
						+ "Congratulations!!! " + str(member['Name']) + " is member of " + str(teamname).upper() + "!" + "\n"*2
						+ "Please verify important membership data:" + "\n"
						+ "- Player's name: "  	+ str(member['Name']) + "\n"
						+ "- Member of team: " 	+ str(teamname) + "\n"
						+ "- Height in inches: " 	+ str(member['Height (inches)']) + "\n"
						+ "- Soccer Experience: " + str(member['Soccer Experience']) + "\n"
						+ "- Guardian Name(s): "  + str(member['Guardian Name(s)']) + "\n"
						+ "- First practice: "  + str(time.strftime("%c"))
						+ "\n"*2
						+ "Best," + "\n" + "Soccer League" 
			)
			
			file.write("\n") # delimiter between teams

		
	# read the list of signed up soccer players
	PLAYERS = read_file()

	# sort players and define three teams
	Dragons, Sharks, Raptors = create_teams(PLAYERS)

	# cretae list of teams and team's members
	write_teams_to_file({'Dragons': Dragons}, {'Sharks' : Sharks}, {'Raptors' : Raptors})

	# mailer




