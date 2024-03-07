def number_scrabble():
    # Make a list of numbers from 1 to 9
    numbers_list = list(range(1, 10))

    # initialize empty lists to store the numbers that each player choose
    player1_numbers = []
    player2_numbers = []

    # This variable is used later to keep track of the current player 1 or 2 
    player_turn = 1

    # Continue the game until all numbers are used
    while numbers_list:

        # Display the remaining numbers
        print("\n"+"Available Numbers:", numbers_list)

        # User input to let the players in their turns to choose a number
        num = int(input("\n"+"Player {} pick a number: ".format(player_turn)))
        print("_______________________________")
        
        # This checks if the chosen number is in the numbers list 
        if num in numbers_list:

            # This removes the chosen number from the numbers list
            numbers_list.remove(num)

            # This adds(stores) the chosen number of the players to the empty list of each one that were previously intialized 
            if player_turn == 1:
                player1_numbers.append(num)
            else:
                player2_numbers.append(num)

            # This checks if any player has reached 15
            if sum(player1_numbers) == 15:
                print("Player 1 wins!")
                return
            elif sum(player2_numbers) == 15:
                print("Player 2 wins!")
                return
           
            # switches to the other player for the next turn
            player_turn = 3 - player_turn
        else:
            # this makes sure that the chosen number is in the numbers list
            print("This number is not in the shown numbers, pick again.")
    
    # If all numbers are used and no player has reached 15 them it's a draw
    print("It's a draw!")

number_scrabble()
