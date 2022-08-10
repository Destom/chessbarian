import classes


my_board= classes.Board(5)
barian = classes.Barian(my_board)
my_board.put_piece(barian)

master_creature = classes.creature(my_board,1)

print('welcome to Chessbarian')
while barian.alive:
    my_board.print_board()
    barian.barian_move(my_board)
    #barian.alive = False
