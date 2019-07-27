import sys
import numpy as np
class Board:

    def __init__(self):
        # init empty board
        self.board_array = np.zeros(9,dtype=int)
        self.phase = 0

    def __str__(self):
        out = str(self.board_array[0]) + '------' + str(self.board_array[1]) + '------' + str(self.board_array[2]) + '\n' \
            + '|      |      |\n' \
            + str(self.board_array[3]) + '------' + str(self.board_array[4]) + '------' + str(self.board_array[5]) + '\n' \
            + '|      |      |\n' \
            + str(self.board_array[6]) + '------' + str(self.board_array[7]) + '------' + str(self.board_array[8]) + '\n'
        return out

    def place_marker(self,pos, player_num):
        # Check if position is vacant
        if self.board_array[pos] == 0:
            self.board_array[pos] == player_num
        else:
            print('Position already set on board!')
            return False
        return True

    def move_marker(self,FROM, TO):
        print('test')
        if self.board_array[FROM] == 0:
            print('No marker at from position')
            return False
        if self.board_array[TO] != 0:
            print('TO position already used')
            return False
        # change markers
        self.board_array[TO],self.board_array[FROM] = self.board_array[FROM],self.board_array[TO]
        return True

if __name__ == '__main__':
    b = Board()
    print(b)
