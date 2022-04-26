from board import Board
from setup import Setup
from testWin import testWin
from testBoard import testBoard
from testSetup import testSetup
from integrationTestConnectFour import testConnectFour

#################################################################################
#Unit Test
print("\n")
print("----------------------------------------------------------")
print("\t\t\t\t\t Unit Test \t\t\t\t\t\t")
print("----------------------------------------------------------")
testwin = testWin()
testwin.test_successful_horizontal_winning_move_is_found()
testwin.test_successful_vertical_winning_move_is_found()
testwin.test_successful_diagonal1_winning_move_is_found()
testwin.test_successful_diagonal2_winning_move_is_found()
testwin.test_is_win_not()

testboard = testBoard()
testboard.test_board_starts_empty()
testboard.test_get_cell()
testboard.test_is_board_full()
testboard.test_drop_disc()
testboard.test_discs_are_dropped_in_separate_columns()

testsetup = testSetup()
testsetup.test_get_players()
testsetup.test_choose_name_color()

#################################################################################
#Integration Test
print("\n")
print("----------------------------------------------------------")
print("\t\t\t\t\t Integration Test \t\t\t\t\t\t")
print("----------------------------------------------------------")
testConnectFour = testConnectFour()
testConnectFour.test_connect_four()
testConnectFour.test_different_discs_are_dropped_in_separate_columns()
testConnectFour.test_setup_players()
testConnectFour.test_draw_game()
testConnectFour.test_illegal_move()

#################################################################################
#Connect Four Game

print("\n")
print("----------------------------------------------------------")
print("\t\t\t\t\t Connect Four \t\t\t\t\t\t")
print("----------------------------------------------------------")
if __name__ == '__main__':
	player_setup = Setup()
	
	# game loop
	play_again = 'yes'
	while play_again in Setup.ACCEPTABLE_ANSWERS:
		player_setup.run(True)
		height, width = Board.get_dimensions()
		connect_four_game = Board(player_setup.get_players(), height, width)
		connect_four_game.play()
		play_again = str(input("Would you like to play again?: \n")).strip().lower()
  
print('\nThanks for playing!')
print('Exiting...\n')