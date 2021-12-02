        import random
        import round
#i hope that syncing works with atom now as well

# this belongs together (find a more stylish implementation) --> I found a more stylish implementation
	class seed_randomness():
		
		def seeding_randomness():
			global user_seed


			user_decision = input("If you want, you can enter a seed for the randomizers in this program.\nDo you want to enter a seed?\n(y)es/(n)o")

			if user_decision = "y" or "yes":
				user_seed = input("Please enter the seed you want to use (!only numbers allowed!): ")
			else:
				print("The system will use the default value.\n\n Enjoy the game!")

			try:
				seed(user_seed)
				print("Your seed has been applied!\n\nEnjoy the game!")
			else:
				print("Sorry! Your seed could not be applied, using default value.\n\nEnjoy the game!")



	class active_world:

# the field has a range of 6x6 cells for each biome, biomes are divided by a line of cells (neutral ground) that lead to the center city (hub)
# each cell has a unique number (counting from the left downwards and starting at 1 for every biome)
# each biome is divided into quadrants again, meaning a biome consists of 4x(3x3) cells (NOTE: create the cells as classes so you can keep the atributes and use parameters for customization)


# all the things that belong into biomes_class -- functions for what the cells are? (maybe | UPDATE: definetly) -- one-time-events/all possible events --

# BIOME ORDER: >top left - forest< | >top right - mountains< | >bottom left - desert< | >bottom right - swamps<
	class forest_biome:
		global player_location
		global forest_1
		global forest_2
		global forest_3
		global forest_4



	class desert_biome:
		global player_location
		global desert_1
		global desert_2
		global desert_3
		global desert_4



	class mountain_biome:
		global player_location
		global mountains_1
		global mountains_2
		global mountains_3
		global mountains_4



	class swamps_biome:
		global player_location
		global swamps_1
		global swamps_2
		global swamps_3
		global swamps_4




	class Cell:
		global player_location
		global active_biome
		global option_N
		global option_E
		global option_S
		global option_W
# every biome is now grouped with its custom locations - the center fields are grouped seperately


		def player_location(self):
			global player_location
			global active_biome
			global option_N
			global option_E
			global option_S
			global option_W


			if player_location = 8:
				option_N = 2
				option_E = 9
				option_S = 14
				option_W = 7
			elif player_location = 9:
				option_N = 3
				option_E = 10
				option_S = 15
				option_W = 8
			elif player_location = 10:
				option_N = 4
				option_E = 11
				option_S = 16
				option_W = 9
			elif player_location = 11:
				option_N = 5
				option_E = 12
				option_S = 17
				option_W = 10
			elif player_location = 14:
				option_N = 8
				option_E = 15
				option_S = 20
				option_W = 13
			elif player_location = 15:
				option_N = 9
				option_E = 16
				option_S = 21
				option_W = 14
			elif player_location = 16:
				option_N = 10
				option_E = 17
				option_S = 22
				option_W = 15
			elif player_location = 17:
				option_N = 11
				option_E = 18
				option_S = 23
				option_W = 16
			elif player_location = 20:
				option_N = 14
				option_E = 21
				option_S = 26
				option_W = 19
			elif player_location = 21:
				option_N = 15
				option_E = 22
				option_S = 27
				option_W = 20
			elif player_location = 22:
				option_N = 16
				option_E = 23
				option_S = 28
				option_W = 21
			elif player_location = 23:
				option_N = 17
				option_E = 24
				option_S = 29
				option_W = 22
			elif player_location = 26:
				option_N = 20
				option_E = 27
				option_S = 32
				option_W = 25
			elif player_location = 27:
				option_N = 21
				option_E = 28
				option_S = 33
				option_W = 26
			elif player_location = 28:
				option_N = 22
				option_E = 29
				option_S = 34
				option_W = 27
			elif player_location = 29:
				option_N = 23
				option_E = 30
				option_S = 35
				option_W = 28


			elif player_location = 1 and active_biome = forest_biome:
				option_N = 0
				option_E = 2
				option_S = 7
				option_W = 0
			elif player_location = 2 and active_biome = forest_biome:
				option_N = 0
				option_E = 3
				option_S = 8
				option_W = 1
			elif player_location = 3 and active_biome = forest_biome:
				option_N = 0
				option_E = 4
				option_S = 10
				option_W = 2
			elif player_location = 4 and active_biome = forest_biome:
				option_N = 0
				option_E = 5
				option_S = 11
				option_W = 3
			elif player_location = 5 and active_biome = forest_biome:
				option_N = 0
				option_E = 6
				option_S = 11
				option_W = 4
			elif player_location = 6 and active_biome = forest_biome:
				option_N = 0
				option_E = N6
				option_S = 7
				option_W = 5
			elif player_location = 7 and active_biome = forest_biome:
				option_N = 1
				option_E = 8
				option_S = 13
				option_W = 0
			elif player_location = 12 and active_biome = forest_biome:
				option_N = 6
				option_E = N5
				option_S = 18
				option_W = 11
			elif player_location = 13 and active_biome = forest_biome:
				option_N = 7
				option_E = 14
				option_S = 19
				option_W = 0
			elif player_location = 18 and active_biome = forest_biome:
				option_N = 12
				option_E = N4
				option_S = 24
				option_W = 17
			elif player_location = 19 and active_biome = forest_biome:
				option_N = 13
				option_E = 20
				option_S = 25
				option_W = 0
			elif player_location = 24 and active_biome = forest_biome:
				option_N = 18
				option_E = N3
				option_S = 30
				option_W = 23
			elif player_location = 25 and active_biome = forest_biome:
				option_N = 19
				option_E = 26
				option_S = 31
				option_W = 0
			elif player_location = 30 and active_biome = forest_biome:
				option_N = 24
				option_E = N2
				option_S = 36
				option_W = 29
			elif player_location = 31 and active_biome = forest_biome:
				option_N = 25
				option_E = 32
				option_S = W6
				option_W = 0
			elif player_location = 32 and active_biome = forest_biome:
				option_N = 26
				option_E = 33
				option_S = W5
				option_W = 31
			elif player_location = 33 and active_biome = forest_biome:
				option_N = 27
				option_E = 34
				option_S = W4
				option_W = 32
			elif player_location = 34 and active_biome = forest_biome:
				option_N = 28
				option_E = 35
				option_S = W3
				option_W = 33
			elif player_location = 35 and active_biome = forest_biome:
				option_N = 29
				option_E = 36
				option_S = W2
				option_W = 34
			elif player_location = 36 and active_biome = forest_biome:
				option_N = 30
				option_E = N1
				option_S = W1
				option_W = 35


			elif player_location = 1 and active_biome = mountain_biome:
				option_N = 0
				option_E = 2
				option_S = 7
				option_W = N6
			elif player_location = 2 and active_biome = mountain_biome:
				option_N = 0
				option_E = 3
				option_S = 8
				option_W = 1
			elif player_location = 3 and active_biome = mountain_biome:
				option_N = 0
				option_E = 4
				option_S = 9
				option_W = 2
			elif player_location = 4 and active_biome = mountain_biome:
				option_N = 0
				option_E = 5
				option_S = 10
				option_W = 3
			elif player_location = 5 and active_biome = mountain_biome:
				option_N = 0
				option_E = 6
				option_S = 11
				option_W = 4
			elif player_location = 6 and active_biome = mountain_biome:
				option_N = 0
				option_E = 0
				option_S = 12
				option_W = 5
			elif player_location = 7 and active_biome = mountain_biome:
				option_N = 1
				option_E = 8
				option_S = 13
				option_W = N5
			elif player_location = 12 and active_biome = mountain_biome:
				option_N = 6
				option_E = 0
				option_S = 18
				option_W = 11
			elif player_location = 13 and active_biome = mountain_biome:
				option_N = 7
				option_E = 14
				option_S = 19
				option_W = N4
			elif player_location = 18 and active_biome = mountain_biome:
				option_N = 12
				option_E = 0
				option_S = 24
				option_W = 17
			elif player_location = 19 and active_biome = mountain_biome:
				option_N = 13
				option_E = 20
				option_S = 25
				option_W = N3
			elif player_location = 24 and active_biome = mountain_biome:
				option_N = 18
				option_E = 0
				option_S = 30
				option_W = 23
			elif player_location = 25 and active_biome = mountain_biome:
				option_N = 19
				option_E = 26
				option_S = 31
				option_W = N2
			elif player_location = 30 and active_biome = mountain_biome:
				option_N = 24
				option_E = 0
				option_S = 36
				option_W = 29
			elif player_location = 31 and active_biome = mountain_biome:
				option_N = 25
				option_E = 32
				option_S = E1
				option_W = N1
			elif player_location = 32 and active_biome = mountain_biome:
				option_N = 26
				option_E = 33
				option_S = E2
				option_W = 31
			elif player_location = 33 and active_biome = mountain_biome:
				option_N = 27
				option_E = 34
				option_S = E3
				option_W = 32
			elif player_location = 34 and active_biome = mountain_biome:
				option_N = 28
				option_E = 35
				option_S = E4
				option_W = 33
			elif player_location = 35 and active_biome = mountain_biome:
				option_N = 29
				option_E = 36
				option_S = E5
				option_W = 34
			elif player_location = 36 and active_biome = mountain_biome:
				option_N = 30
				option_E = 0
				option_S = E6
				option_W = 35


			elif player_location = 1 and active_biome = desert_biome:
				option_N = W6
				option_E = 2
				option_S = 7
				option_W = 0
			elif player_location = 2 and active_biome = desert_biome:
				option_N = W5
				option_E = 3
				option_S = 8
				option_W = 1
			elif player_location = 3 and active_biome = desert_biome:
				option_N = W4
				option_E = 4
				option_S = 9
				option_W = 2
			elif player_location = 4 and active_biome = desert_biome:
				option_N = W3
				option_E = 5
				option_S = 10
				option_W = 3
			elif player_location = 5 and active_biome = desert_biome:
				option_N = W2
				option_E = 6
				option_S = 11
				option_W = 4
			elif player_location = 6 and active_biome = desert_biome:
				option_N = W1
				option_E = S1
				option_S = 12
				option_W = 5
			elif player_location = 7 and active_biome = desert_biome:
				option_N = 1
				option_E = 8
				option_S = 13
				option_W = 0
			elif player_location = 12 and active_biome = desert_biome:
				option_N = 6
				option_E = S2
				option_S = 18
				option_W = 11
			elif player_location = 13 and active_biome = desert_biome:
				option_N = 7
				option_E = 14
				option_S = 19
				option_W = 0
			elif player_location = 18 and active_biome = desert_biome:
				option_N = 12
				option_E = S3
				option_S = 24
				option_W = 17
			elif player_location = 19 and active_biome = desert_biome:
				option_N = 13
				option_E = 20
				option_S = 25
				option_W = 0
			elif player_location = 24 and active_biome = desert_biome:
				option_N = 18
				option_E = S4
				option_S = 30
				option_W = 23
			elif player_location = 25 and active_biome = desert_biome:
				option_N = 19
				option_E = 26
				option_S = 31
				option_W = 0
			elif player_location = 30 and active_biome = desert_biome:
				option_N = 24
				option_E = S5
				option_S = 36
				option_W = 29
			elif player_location = 31 and active_biome = desert_biome:
				option_N = 25
				option_E = 32
				option_S = 0
				option_W = 0
			elif player_location = 32 and active_biome = desert_biome:
				option_N = 26
				option_E = 33
				option_S = 0
				option_W = 31
			elif player_location = 33 and active_biome = desert_biome:
				option_N = 27
				option_E = 34
				option_S = 0
				option_W = 32
			elif player_location = 34 and active_biome = desert_biome:
				option_N = 28
				option_E = 35
				option_S = 0
				option_W = 33
			elif player_location = 35 and active_biome = desert_biome:
				option_N = 29
				option_E = 36
				option_S = 0
				option_W = 34
			elif player_location = 36 and active_biome = desert_biome:
				option_N = 30
				option_E = S6
				option_S = 0
				option_W = 35

			elif player_location = 1 and active_biome = swamps_biome:
				option_N = E1
				option_E = 2
				option_S = 7
				option_W = S1
			elif player_location = 2 and active_biome = swamps_biome:
				option_N = E2
				option_E = 3
				option_S = 8
				option_W = 1
			elif player_location = 3 and active_biome = swamps_biome:
				option_N = E3
				option_E = 4
				option_S = 9
				option_W = 2
			elif player_location = 4 and active_biome = swamps_biome:
				option_N = E4
				option_E = 5
				option_S = 10
				option_W = 3
			elif player_location = 5 and active_biome = swamps_biome:
				option_N = E5
				option_E = 6
				option_S = 11
				option_W = 4
			elif player_location = 6 and active_biome = swamps_biome:
				option_N = E6
				option_E = 0
				option_S = 12
				option_W = 5
			elif player_location = 7 and active_biome = swamps_biome:
				option_N = 1
				option_E = 8
				option_S = 13
				option_W = S2
			elif player_location = 12 and active_biome = swamps_biome:
				option_N = 6
				option_E = 0
				option_S = 18
				option_W = 11
			elif player_location = 13 and active_biome = swamps_biome:
				option_N = 7
				option_E = 14
				option_S = 19
				option_W = S3
			elif player_location = 18 and active_biome = swamps_biome:
				option_N = 12
				option_E = 0
				option_S = 24
				option_W = 17
			elif player_location = 19 and active_biome = swamps_biome:
				option_N = 13
				option_E = 20
				option_S = 25
				option_W = S4
			elif player_location = 24 and active_biome = swamps_biome:
				option_N = 18
				option_E = 0
				option_S = 30
				option_W = 23
			elif player_location = 25 and active_biome = swamps_biome:
				option_N = 19
				option_E = 26
				option_S = 31
				option_W = S5
			elif player_location = 30 and active_biome = swamps_biome:
				option_N = 24
				option_E = 0
				option_S = 36
				option_W = 29
			elif player_location = 31 and active_biome = swamps_biome:
				option_N = 25
				option_E = 32
				option_S = 0
				option_W = S6
			elif player_location = 32 and active_biome = swamps_biome:
				option_N = 26
				option_E = 33
				option_S = 0
				option_W = 31
			elif player_location = 33 and active_biome = swamps_biome:
				option_N = 27
				option_E = 34
				option_S = 0
				option_W = 32
			elif player_location = 34 and active_biome = swamps_biome:
				option_N = 28
				option_E = 35
				option_S = 0
				option_W = 33
			elif player_location = 35 and active_biome = swamps_biome:
				option_N = 29
				option_E = 36
				option_S = 0
				option_W = 34
			elif player_location = 36 and active_biome = swamps_biome:
				option_N = 30
				option_E = 0
				option_S = 0
				option_W = 35


	# thinking of a way to put the neutral ground into different clauses that look a little better (something like if player_location = N3 and player_selection = north: option_N)
			elif player_location = G0:
				option_N = N1
				option_E = E1
				option_S = S1
				option_W = W1


			elif player_location = N1:
				option_N = N2
				option_E = 31
				option_S = G0
				option_W = 36
			elif player_location = N2:
				option_N = N3
				option_E = 25
				option_S = N2
				option_W = 30
			elif player_location = N3:
				option_N = N4
				option_E = 19
				option_S = N2
				option_W = 24
			elif player_location = N4:
				option_N = N5
				option_E = 13
				option_S = N3
				option_W = 18
			elif player_location = N5:
				option_N = N6
				option_E = 7
				option_S = N4
				option_W = 12
			elif player_location = N6:
				option_N = 0
				option_E = 1
				option_S = N5
				option_W = 6


			elif player_location = E1:
				option_N = 31
				option_E = E2
				option_S = 1
				option_W = G0
			elif player_location = E2:
				option_N = 32
				option_E = E3
				option_S = 2
				option_W = E1
			elif player_location = E3:
				option_N = 33
				option_E = E4
				option_S = 3
				option_W = E2
			elif player_location = E4:
				option_N = 34
				option_E = E5
				option_S = 4
				option_W = E3
			elif player_location = E5:
				option_N = 35
				option_E = E6
				option_S = 5
				option_W = E4
			elif player_location = E6:
				option_N = 36
				option_E = 0
				option_S = 6
				option_W = E5


			elif player_location = S1:
				option_N = G0
				option_E = 1
				option_S = S2
				option_W = 6
			elif player_location = S2:
				option_N = S1
				option_E = 7
				option_S = S3
				option_W = 12
			elif player_location = S3:
				option_N = S2
				option_E = 13
				option_S = S4
				option_E = 18
			elif player_location = S4:
				option_N = S3
				option_E = 19
				option_S = S4
				option_W = 24
			elif player_location = S5:
				option_N = S4
				option_E = 25
				option_S = S6
				option_W = 30
			elif player_location = S6:
				option_N = S5
				option_E = 31
				option_S = 0
				option_W = 36


			elif player_location = W1:
				option_N = 36
				option_E = G0
				option_S = 6
				option_W = W2
			elif player_location = W2:
				option_N = 35
				option_E = W1
				option_S = 5
				option_W = W3
			elif player_location = W3:
				option_N = 34
				option_E = W2
				option_S = 4
				option_W = W4
			elif player_location = W4:
				option_N = 33
				option_E = W3
				option_S = 3
				option_W = W5
			elif player_location = W5:
				option_N = 32
				option_E = W4
				option_S = 2
				option_W = W6
			elif player_location = W6:
				option_N = 31
				option_E = W5
				option_S = 1
				option_W = 0



	class Player:

		def global_menu(self):
			global_input = input("What do you want to do?")

		def battle_menu(self):
			battle_input = input("What do you want to do?\n[a] Attack\n[b] Defend\n[c] Use an Item\n[d] Run")

			if battle_input = "a":
				attack()
			elif battle_input = "b":
				defend()
			elif battle_input = "c":
				item_menu()
			elif battle_input = "d":
				run_prob = randint(1, 10)
			if run_prob = 1:
				run = 1
			else:
				run = 0
			if run = 1:
				print("You successfully fled from battle!")
				global_menu()
			else:
				print("Please make a valid selection")
				battle_menu()



		def movement_menu(self):
			global option_N
			global option_E
			global option_S
			global option_W

			movement_input = input("Which way do you want to move?\n\n[a] Head north\n[b] Head east\n[c] Head south\n[d] Head west\n\n[e] Do something else\n")

			if movement_input = "a":
				if option_N = 0:
					print("There seems to be no possibility to move that way...")
					movement()
				else:
					movement_selection = option_N
			
			elif movement_input = "b":
				if option_E = 0:
					print("There seems to be no possibility to move that way...")
					movement()
				else:
					movement_selection = option_E
			
			elif movement_input = "c":
				if option_S = 0:
					print("There seems to be no possibility to move that way...")
					movement()
				else:
					movement_selection = option_S

			elif movement_input = "d":
				if option_W = 0:
					print("There seems to be no possibility to move that way...")
					movement()
				else:
					movement_selection = option_W
				
			elif movement_input = "e":
				global_menu()
			else:
				print("Please make a valid selection!\n")
				movement_menu()



# here I need a try function to test if the user input was valid to the possible actions displayed before
# to make sure the player cannot redo a one-time-event, a variable will be set from 0 to 1 to indicate that it has been done once already and is not available for selection again

#first try on a function to choose which enemy to use (each of the 4 biomes get 4 possible sets of enemies that can appear in the corresponding quadrant + some unique enemies for one-time-events)
	class RNG_system:

		def choose_enemy(self):
			global enemy_lvl
			global encounter
			global player_level
			global active_sector
			enemy_lvl = player_level randint(-1, 2)

# thinking if it works to make an if-clause that chooses from a list of enemies so I only assign values to a list of enemies and dont have to create an own clause for each possible enemy
			if active_sector == forest_1 or desert_1 or mountains_1 or swamps_1:
				encounter = randint(1, 3)

			elif active_sector == forest_2 or desert_2 or mountains_2 or swamps_2:
				encounter = randint(4, 6)

			elif active_sector == forest_3 or desert_3 or mountains_3 or swamps_3:
				encounter = randint(7, 9)

			elif active_sector == forest_4 or desert_4 or mountains_4 or swamps_4:
				encounter = randint(10, 12)
		
		
		def enemy_listing(self):
			global encounter
			global active_biome
			global set_1
			global set_2
			global set_3
			global set_4
			
			encounter_val = encounter


			set_1 = [fe1, fe2, fe3,  fe4, fe5, fe6,  fe7, fe8, fe9,  fe10, fe11, fe12]
			set_2 = [de1, de2, de3,  de4, de5, de6,  de7, de8, de9,  de10, de11, de12]
			set_3 = [me1, me2, me3,  me4, me5, me6,  me7, me8, me9,  me10, me11, me12]
			set_4 = [se1, se2, se3,  se4, se5, se6,  se7, se8, se9,  se10, se11, se12]


			if active_biome = forest_biome:
				encounter_set = forest_set

			elif active_biome = desert_biome:
				encounter_set = desert_set

			elif active_biome = mountain_biome:
				encounter_set = mountain_set

			elif active_biome = swamps_biome:
				encounter_set = swamps_set


			final_encounter = encounter_set[encounter_val - 1]

# listing enemy sets for each sector (seperated by biomes)

				
	class enemy_base:
		global set_1
		global set_2
		global set_3
		global set_4
		global base_hp
		global base_lvl
		
		base_hp = 20
		base_lvl = 1
		
		
		def enemy_form(self):
			global variation
			
			variation_value = randint(1,5)
			
			if variation_value = 1 or 2:
				variation = "lesser"
			elif variation_value = 3 or 4:
				variation = "normal"
			elif variation_value = 5:
				variation = "savage"
				
			if variation = "lesser":
				enemy_hp = enemy_hp * .8
				enemy
		
		def determine_atk(self):
			global enemy_lvl
			global atk_value
			
			atk_base = randint(1, 3)
			atk_value = round(atk_base * (1.2 * enemy_lvl))

#if you rewrite the lists for enemy selections and group them by biomes instead of sectors, you can put enemy selection into one single if-clause (if biome == forest_1 or desert_1 or mountains_1 or swamps_1: encounter_1 = randint(1, 3) || same for the other 3 encounters) -- DONE (looks much better now)

		





    # for the enemy classes
		
