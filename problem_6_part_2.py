"""
Assignment: Residency Problem Set (Part 2)
Description:  Program to play Ghost word game for two players 
Created Date: 11/18/2023
Last Modified: 11/18/2023
Authors: Nongnapat Throngprasertchai, Sandhya Rani Alavala, Syed Mujahid Ali, Vinu Prasad Bhambore
"""

def import_wordlist(file_path):  
    """
    This function imports a list of words from an external file and processes them.
    Inputs: 
        1. 'file_path' (string) : The string that represents the path of the file to be imported
    Output: 
        1. 'word_list' (list): List of valid words from the file in lowercase
    """

    with open(file_path, 'r') as file:                                      #Open the file in the path in read mode
        word_list = [line.strip().lower() for line in file.readlines()]     #Reading each word line by line, converting it into lowercase and storing it in a list
        
    return word_list                                                        #Return the word list created

def play_ghost_game(word_list):
    """
    This is the main function to play the Ghost game. It manages game state, player turns, input validation, and win/loss conditions.
    Inputs: 
        1. 'word_list' (list) : List of valid words from the file
    Output: None
    """
    current_fragment = ''                   #Declaring a variable to the store the current string, initializing it to empty string at start of the game
    current_player = 1                      #Declaring a variable to indicate the player making the move, initializing to player 1 at start of the game

    while True:                                                                                 #Loop to keep the game running until it ends
        print(f"Player {current_player}'s turn. Current word fragment: '{current_fragment}'")   #Printing the current player and word
        letter = input(f"Player {current_player}, enter your letter: ").lower()                 #The new letter input from the player

        if not letter.isalpha() or len(letter) != 1:                                            #If the input is not an alphabet or is empty
            print("Invalid input. Please enter a single letter.")                               #Display error
            continue                                                                            #Continue the loop

        current_fragment += letter                                                              #Adding the new letter to the current fragment

        if len(current_fragment) >= 4 and current_fragment in word_list:                            #If the word length > 4 and the word is valid
            print(f"{current_fragment.capitalize()} is a word! Player {3 - current_player} wins.")  #Announce the winner
            break                                                                                   #Break the loop
        elif not any(word.startswith(current_fragment) for word in word_list):                      #If there is no word starting with current fragment
            print(f"No words start with '{current_fragment}'. Player {3 - current_player} wins.")   #Display message that the word is invalid and announce the winner
            break                                                                                   #Break the loop

        current_player = 3 - current_player                                                      #Switch the player for next round

if __name__ == "__main__":
    word_list = import_wordlist('words.txt')       #Create the word list from the file given
    play_ghost_game(word_list)                     #Start the game
