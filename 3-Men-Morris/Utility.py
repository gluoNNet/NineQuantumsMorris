import copy

def numOfValue(board, value):
    return board.count(value)

def InvertedBoard(board):
    invertedboard = []
    for i in board:
        if i == "₣":
            invertedboard.append("€")
        elif i == "€":
            invertedboard.append("₣")
        else:
            invertedboard.append("X")
    return invertedboard

def generateInvertedBoardList(pos_list):
    '''
    '''
    result = []
    for i in pos_list:
        result.append(InvertedBoard(i))
    return result
