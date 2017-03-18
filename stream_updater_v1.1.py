print("Welcome to Smash 4 stream updater :)")
print("v 1.1 by Alonzo Castanon (github.com/alonzoc1)")
import os
import shutil
path = os.getcwd()
path += "\\Ico\\"

s = 'init'
while (s != 'q'):
	i = input("Input Player 1's tag: ")
	player1 = open('player1.txt', 'w')
	player1.write(i)
	player1.close()
	i = input("Input Player 2's tag: ")
	player2 = open('player2.txt', 'w')
	player2.write(i)
	player2.close()
	i = input("Input Player 1's set count: ")
	set1 = open('set1.txt', 'w')
	set1.write(i)
	set1.close()
	i = input("Input Player 2's set count: ")
	set2 = open('set2.txt', 'w')
	set2.write(i)
	set2.close()
	i = input ("Input Match Title (eg. Winners Finals): ")
	match = open('match.txt', 'w')
	match.write(i)
	match.close()
	i = input("Input Character Name 1 (for help on this type 'h'): ")
	if (i == 'h'):
		print("Character names are typically all lowercase and spaced with '_'")
		print("For example, 'captain_falcon', 'kirby', 'bowser_jr', 'dr_mario'")
		print("For Robin and Corrin type 'corrin_boi', or 'robin_gril'")
		print("For Zero Suit Samus type 'zss'")
		print("Finally, for Wii Fit Trainer(s) type 'wft_boi' or 'wft_gril'")
		print("Here are all valid inputs:")
		for file in os.listdir(path):
			if (file.endswith('.png')):
				print(file)
		i = input("Input Character Name: ")
	try:
		i += '.png'
		path2 = path+i
		path3 = path+'current1.png'
		shutil.copyfile(path2, path3)
	except Exception as inst:
		print(i, "not found, keeping current...")
		print(type(inst))
		print(inst.args)
		print(inst)
		print("To try again, just start a new game ;)")
	i = input("Input Character Name 2 (for help on this type 'h'): ")
	if (i == 'h'):
		print("Character names are typically all lowercase and spaced with '_'")
		print("For example, 'captain_falcon', 'kirby', 'bowser_jr', 'dr_mario'")
		print("For Robin and Corrin type 'corrin_boi', or 'robin_gril'")
		print("For Zero Suit Samus type 'zss'")
		print("Finally, for Wii Fit Trainer(s) type 'wft_boi' or 'wft_gril'")
		print("Here are all valid inputs:")
		for file in os.listdir(path):
			if (file.endswith('.png')):
				print(file)
		i = input("Input Character Name: ")
	try:
		i += '.png'
		path2 = path+i
		path3 = path+'current2.png'
		shutil.copyfile(path2, path3)
	except:
		print(i, "not found, keeping current...")
		
		print("To try again, just start a new game ;)")
	print("All details entered! :)")
	i = input("For new game, type 'n', to update set count only type 's', to quit type 'q': ")
	if (i == 'q'):
		s = 'q'
	if (i == 's'):
		b = 'init'
		while (b != 'q'):
			print("Updating set count!")
			i = input("Input Player 1's set count: ")
			set3 = open("set1.txt", 'w')
			set3.write(i)
			set3.close()
			i = input("Input Player 2's set count: ")
			set4 = open("set2.txt", 'w')
			set4.write(i)
			set4.close()
			print("Set counts updated!")
			i = input("For a new game, type 'n', to update set count again type 's', to quit type 'q': ")
			if (i == 'n'):
				b = 'q'
			if (i == 'q'):
				b = 'q'
				s = 'q'
	if (s != 'q'):
		print("Starting new game...")
	if (s == 'q'):
		print("Quitting...")
