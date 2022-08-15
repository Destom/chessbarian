import classes

### Game options ###
board_size = 5
creature_count = 3

my_board= classes.Board(board_size)
barian = classes.Barian(my_board)
my_board.put_piece(barian)

creature_list = []
for creature in range(1,creature_count +1):
    creature_list.append(classes.Creature(my_board,creature))
    print (creature)

print('welcome to Chessbarian')
while barian.alive:
    print('Board as it stands')
    my_board.print_board()
    for creature in creature_list:
        creature.printCreatureState()
    barian.barian_move(my_board)
    print('''Creature status currently stands at:}''')

    #barian.alive = False