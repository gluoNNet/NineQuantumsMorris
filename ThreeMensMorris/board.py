import sys
import numpy as np
class Board:

    def __init__(self):
        # init empty board
        self.board_array = np.zeros(9,dtype=int)
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
        if self.board_array[pos] == 0:
            self.board_array[pos] = player_num
        else:
            print('Position already set on board!')
            return False
        self.check_mill()
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
        self.check_mill()
        return True

    def check_mill(self):
        neighbors = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]
        ]
        for neighbor in neighbors:
            if self.board_array[neighbor].all() == 1:
                print(self)
                sys.exit('Player number 1 wins!')
            if self.board_array[neighbor].all() == 2:
                print(self)
                sys.exit('Player number 2 wins!')

if __name__ == '__main__':
    b = Board()
    print(b)
    b.place_marker(pos=0,player_num=1)
    b.place_marker(pos=1,player_num=1)
    b.place_marker(pos=2,player_num=1)
    print(b)

    print(b)
