import classes

### Game options ###
board_size = 5
creature_count = 1

#initalizing game
alive_count = 0
my_board= classes.Board(board_size)
barian = classes.Barian(my_board)
my_board.put_piece(barian)
creature_list = []
for creature in range(1,creature_count +1):
    creature_list.append(classes.Creature(my_board,creature,'king'))
    alive_count +=1


print('welcome to Chessbarian')
while barian.alive and alive_count > 0:
    print('Board as it stands')
    my_board.print_board()
    for creature in creature_list:   
        creature.printCreatureState()
    barian.barian_move(my_board,creature_list)
    alive_count = 0
    for creature in creature_list:
        if creature.alive:
            alive_count += 1
            creature.moveCreature(my_board, barian)

if barian.alive == False:
    print('The barbarian is dead long live the barbarian')
elif alive_count == 0:
    print('you killed all the creatues, yay')
else:
    print('I have no idea why this game ended, maybe you should get a real dev to make your games')