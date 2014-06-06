import os, msvcrt, sys, random

class Punter:
	def __init__(self, name):
		self.name = name
		self.teams = []
	def __str__(self):
		return self.name

seeds = ["Brazil", "Spain", "Germany", "Argentina", "Colombia", "Belgium", "Uruguay", "Switzerland", "Netherlands"]
non_seeds = ["Bosnia and Herzegovina", "Croatia", "England", "France", "Greece", "Italy", "Portugal", "Russia", "Australia", "Iran", "Japan", "South Korea", "Costa Rica", "Honduras", "Mexico", "United States",  "Algeria", "Cameroon", "Ivory Coast", "Ghana", "Nigeria", "Chile", "Ecuador"]

punter_names = ["Zac", "Trent", "Mehta", "Matt", "William", "Duncan", "Dan", "Min", "Paul"]

punters = []

for name in punter_names:
	punters.append(Punter(name))

os.system('cls')
print("*** WELCOME TO THE OFFICIAL D-LINK WORLD CUP SWEEPSTAKES 2014 ***")
print("    ---------------------------------------------------------    \n\n")
msvcrt.getch()
print("May all your footballing dreams come true!\n")
msvcrt.getch()
print("With your host, Zac Blatter.\n")
msvcrt.getch()
sys.stdout.write("LET THE DRAWWWWWWWWW..... ")
sys.stdout.flush()
msvcrt.getch()
sys.stdout.write("COMMENCE!!!")
sys.stdout.flush()
msvcrt.getch()

# Randomise non-seeds!
os.system('cls')
print("Shuffling the pot of non-seeds...")
msvcrt.getch()
os.system('cls')
random.shuffle(punters)
random.shuffle(non_seeds)

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

# Allocate the bulk of the non-seeded teams.
print("First, the non-seeded teams. Let's get the dross out of the way.\n\n")
msvcrt.getch()
while len(non_seeds) >= len(punters):
	for p in punters:
		print(p.name + ", you're up!\n")
		msvcrt.getch()
		print("Drum roll please...\n")
		msvcrt.getch()
		print("You have drawn: ")
		msvcrt.getch()
		t = non_seeds.pop()
		drama_print(t)
		p.teams.append(t)
		os.system('cls')		

# Allocate the final few.
random.shuffle(punters)
print("Now, these lucky people will get an extra team!\n\n")
msvcrt.getch()
for i in range(len(non_seeds)):
	print(punters[i].name + ", you're one of the chosen few to get an extra team!\n")
	msvcrt.getch()
	print("Drum roll please...\n")
	msvcrt.getch()
	print("You have drawn: ")
	msvcrt.getch()
	t = non_seeds.pop()
	drama_print(t)	
	punters[i].teams.append(t)
	os.system('cls')

# All non-seeds assigned.
assert non_seeds == []

# Randomise seeds!
os.system('cls')
print("Shuffling the pot of seeds...")
msvcrt.getch()
os.system('cls')
random.shuffle(punters)
random.shuffle(seeds)

# Allocate a seeded team.
print("And now... THE SEEDED TEAMS!\n\n")
msvcrt.getch()
for p in punters:
	print(p.name + ", you're up!\n")
	msvcrt.getch()
	print("Drum roll please...\n")
	msvcrt.getch()
	print("You have drawn: ")
	msvcrt.getch()
	t = seeds.pop()
	drama_print(t)
	p.teams.append(t)
	os.system('cls')		

# All seeds assigned.
assert seeds == []

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

print("\nThanks for playing!\nThe results will be stored in .txt or .csv file.\n\n")
print("Enjoy World Cup Brazil 2014, and... good luck!\n\n\n")
msvcrt.getch()

# Write the results to a text file.
print("Writing to text file...")
f = open("Sweepstakes.txt", 'w')
for p in punters:
	f.write(p.name + " has drawn:\n")
	for t in p.teams:
		f.write("*  " + t + "\n")
	f.write("\n")
f.close()
print("Complete!\n\n")

# Write the results to a CSV file.
print("Writing to CSV file...")
f = open("Sweepstakes.csv", 'w')
for p in punters:
	f.write(p.name)
	for t in p.teams:
		f.write("," + t)
	f.write("\n")
f.close()
print("Complete!\n\n")