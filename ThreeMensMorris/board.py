import sys
import numpy as np
class Board:

    def __init__(self):
        # init empty board
        self.board_array = np.zeros(9,dtype=int)
        self.num_checkers_one = 0
        self.num_checkers_two = 0
        self.phase = 0

    def __str__(self):
        out = '\n \n' + str(self.board_array[0]) + '------' + str(self.board_array[1]) + '------' + str(self.board_array[2]) + '\n' \
            + '|      |      |\n' \
            + str(self.board_array[3]) + '------' + str(self.board_array[4]) + '------' + str(self.board_array[5]) + '\n' \
            + '|      |      |\n' \
            + str(self.board_array[6]) + '------' + str(self.board_array[7]) + '------' + str(self.board_array[8]) + '\n \n'
        return out

    def place_marker(self,pos, player_num):
        # Check if position is vacant
        if self.board_array[pos] == player_num:
            return True
        if self.board_array[pos] == 0:
            self.board_array[pos] = player_num
            if player_num == 1:
                self.num_checkers_one += 1
            if player_num == 2:
                self.num_checkers_two += 1
        else:
            print('Position already set on board!')
            return False

        self.check_num_markers()
        self.check_mill()
        return True

    def move_marker(self,FROM, TO):
        if self.board_array[FROM] == 0:
            print('No marker at from position')
            return False
        if self.board_array[TO] != 0:
            print('TO position already used')
            return False
        # change markers
        tmp = self.board_array[FROM]
        self.board_array[FROM] = 0
        self.board_array[TO] = tmp
        self.check_mill()
        return True

    def check_mill(self):
        neighbors = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]
        ]
        for neighbor in neighbors:
            if np.array_equal(self.board_array[neighbor],np.array([1,1,1])):
                print(self)
                sys.exit('Player number 1 wins!')
            if np.array_equal(self.board_array[neighbor],np.array([2,2,2])):
                print(self)
                sys.exit('Player number 2 wins!')


    def check_num_markers(self):
        if self.num_checkers_one > 3:
            sys.exit('Player 1 placed too many markers')
        if self.num_checkers_two > 3:
            sys.exit('Player 2 placed too many markers')


if __name__ == '__main__':
    b = Board()
    b.place_marker(pos=0,player_num=1)
    b.place_marker(pos=3,player_num=1)
    b.board_array[0] = 2
    print(b)
    print('Hello')

    #b.place_marker(pos=1,player_num=1)
    #b.place_marker(pos=2,player_num=1)
