import os, msvcrt, sys, random

class Punter:
	def __init__(self, name):
		self.name = name
		self.teams = []
	def __str__(self):
		return self.name

teams = ["Brazil", "Germany", "Argentina", "Colombia", "Belgium", "Netherlands", "France", "Costa Rica"]

# Dictionary as means to check that we're not playing ourselves.
matches = {"Brazil": 1, "Germany": 2, "Argentina": 4, "Colombia": 1, "Belgium": 4, "Netherlands": 3, "France": 2, "Costa Rica": 3}

assert(len(teams) == 8)

punter_names = ["Zac", "Trent", "Matt", "William", "Min", "Paul"]

punters = []

for name in punter_names:
	punters.append(Punter(name))

# Some reckless old sods are betting twice.
double_uppers = [p for p in punters if p.name == "Paul" or p.name == "William"]

assert(len(double_uppers) == 2)

os.system('cls')
print("*** WELCOME TO THE OFFICIAL D-LINK WORLD CUP SWEEPSTAKES 2014 ***")
print("    ---------------------------------------------------------    \n\n")
msvcrt.getch()
print("--- QUARTER FINAL EDITION ---\n")
msvcrt.getch()
print("With your host, Zac \"I love Qatar\" Blatter.\n")
msvcrt.getch()
sys.stdout.write("LET THE DRAWWWWWWWWW..... ")
sys.stdout.flush()
msvcrt.getch()
sys.stdout.write("COMMENCE!!!")
sys.stdout.flush()
msvcrt.getch()

# Randomise pots!
os.system('cls')
print("Processing...\n")
msvcrt.getch()
print("Shuffling the pots...\n")
msvcrt.getch()
print("Matchfixing...\n")
msvcrt.getch()
print("Allocating best team to Zac...\n")
msvcrt.getch()
print("Laughing at Fulham, Australia, USA, and Tottenham...\n")
msvcrt.getch()
print("Hoping that everyone forgets about England...\n")
msvcrt.getch()
print("Reticulating splines...\n")
msvcrt.getch()
print("Solving world poverty...\n")
msvcrt.getch()
print("Ok I'll shut up now...\n")
msvcrt.getch()
os.system('cls')
random.shuffle(punters)
random.shuffle(double_uppers)
random.shuffle(teams)

# Print a word D... R... A... MATICALLY!!!
def drama_print(w):
	sys.stdout.write(w[0])
	sys.stdout.flush()
	msvcrt.getch()
	sys.stdout.write(w[1])
	sys.stdout.flush()
	msvcrt.getch()
	sys.stdout.write(w[2])
	sys.stdout.flush()
	msvcrt.getch()
	print(w[3:] + "!\n\n")
	msvcrt.getch()

# Allocate a single team to each punter.
print("We will now draw one team each.\n\n")
msvcrt.getch()
for p in punters:
	print(p.name + ", you're up!\n")
	msvcrt.getch()
	print("You have drawn: ")
	msvcrt.getch()
	t = teams.pop()
	drama_print(t)
	p.teams.append(t)
	os.system('cls')

# Only 2 teams remain.
assert len(teams) == 2	

# Dish out an extra team to the double-uppers.
print(double_uppers[0].name + " and " + double_uppers[1].name + ", you each get an extra team.\n")
msvcrt.getch()
print("You cannot 'play yourself'. Checking for clashes...\n")
msvcrt.getch()

# As I said, you cannot play yourself.
if matches[double_uppers[0].teams[0]] == matches[teams[1]]:
	print(double_uppers[0].name + " has a clash. Swapping...\n\n")
	msvcrt.getch()
	double_uppers[0].teams.append(teams[0])
	double_uppers[1].teams.append(teams[1])
elif matches[double_uppers[1].teams[0]] == matches[teams[0]]:
	print(double_uppers[1].name + " has a clash. Swapping...\n\n")
	msvcrt.getch()
	double_uppers[0].teams.append(teams[0])
	double_uppers[1].teams.append(teams[1])
else:
	print("There was no clash!\n\n")
	msvcrt.getch()
	double_uppers[0].teams.append(teams[1])
	double_uppers[1].teams.append(teams[0])

# No allocating done here - just for show.
for p in double_uppers:
	print(p.name + ", you're up!\n")
	msvcrt.getch()
	print("You have drawn: ")
	msvcrt.getch()	
	drama_print(p.teams[1])
	os.system('cls')

# Print the results!
print("THE FINAL RESULTS")
print("-----------------\n\n")
msvcrt.getch()
for p in punters:
	print(p.name + " has drawn:")
	for t in p.teams:
		print("*  " + t)
	print()
	msvcrt.getch()

print("\nThanks for playing!\nThe results will be stored in a .txt file.\n\n")
print("Good luck in the Quarter Finals!\n\n\n")
msvcrt.getch()

# Write the results to a text file.
print("Writing to text file...")
f = open("QFSweepstakes.txt", 'w')
for p in punters:
	f.write(p.name + " has drawn:\n")
	for t in p.teams:
		f.write("*  " + t + "\n")
	f.write("\n")
f.close()
print("Complete!\n\n")