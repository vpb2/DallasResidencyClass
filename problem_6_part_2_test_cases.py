"""
Assignment: Residency Problem Set (Part 2)
Description:  Test file for problem_6_part_2 file
Created Date: 11/18/2023
Last Modified: 11/18/2023
Authors: Nongnapat Throngprasertchai, Sandhya Rani Alavala, Syed Mujahid Ali, Vinu Prasad Bhambore
"""
#Importing necessary packages
import unittest
from unittest.mock import patch
from io import StringIO
import os

from problem_6_part_2 import import_wordlist, play_ghost_game

class TestGhostGame(unittest.TestCase):

    def test_import_wordlist(self):
        # Test if the import_wordlist function correctly processes the word list
        test_file = 'test_words.txt'
        with open(test_file, 'w') as f:
            f.write('Apple\nBanana\nCherry\n')
        expected_result = ['apple', 'banana', 'cherry']
        word_list = import_wordlist(test_file)
        os.remove(test_file)  # Clean up the test file
        self.assertEqual(word_list, expected_result)

    @patch('builtins.input', side_effect=['a', 'p', 'p', 'l', 'e'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_logic_win(self, mock_stdout, mock_input):
        # Test if the game logic correctly identifies a win condition
        word_list = ['apple', 'banana', 'cherry']
        play_ghost_game(word_list)
        self.assertIn('Apple is a word! Player 2 wins.', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['x', 'y', 'z'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_logic_invalid_word(self, mock_stdout, mock_input):
        # Test if the game logic correctly identifies an invalid word condition
        word_list = ['apple', 'banana', 'cherry']
        play_ghost_game(word_list)
        self.assertIn("No words start with 'xyz'. Player 2 wins.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
