board = {}
n = int(input('How many queens?'))

def init_board(n):
    for keys in ['queen','rows','col','NwtoSE','SWtoNE']:
        board[keys]={}
    for i in range (n):
        board['queen'][i]=-1
        board['rows'][i]=0
        board['col'][i]=0
    for i in range (-(n-1),n):
        board['NwtoSE'][i]=0
    for i in range (0, 2*n-1):
        board['SWtoNE'][i]=0


def pos_free(row,col):
    return (board['rows'][row] == 0 and
            board['col'][col] == 0 and
            board['NwtoSE'][col-row] == 0 and
            board['SWtoNE'][row+col] == 0)

def fill_queen(row,col):
    board['queen'][row] = col
    board['rows'][row] = 1
    board['col'][col] = 1
    board['NwtoSE'][col-row] = 1
    board['SWtoNE'][row+col] = 1

def undo_queen(row,col):
    board['queen'][row] = -1
    board['rows'][row] = 0
    board['col'][col] = 0
    board['NwtoSE'][col-row] = 0
    board['SWtoNE'][row+col] = 0    

def print_board():
    for i in range (n):
        print ((i,board['queen'][i])) 
    
def place_queen(row):
    n = len(board['queen'].keys())

    for col in range (n):
        if pos_free(row,col):
            fill_queen(row,col)

            if row == (n-1):
                return True
            else:
                extndsoln = place_queen(row+1)
            if extndsoln == True:
                return True
            else:
                undo_queen(row,col)
    else:
        return False
        



init_board(n)
if place_queen(0):
    print_board()
