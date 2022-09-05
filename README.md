# chessbarian

**The Plan**
 - 
**the world**
1. Chess board <br>
    array of arrays always same width and height <br>
2. barian <br>
    able to move like a king at first <br>
    apply other ways of moving when different piece type selected<br>
3. NPCs<br>
    collection of other pieces that can move like chess pieces<br>
    their move is alwas to put the barian in check (hurt on next move) or to get closer to doing it (this should be random not the first option for them)<br>

**the turns**
1. barian moves first using the piece configured (again king by default)
    1. If landing on an enemy piece remove it from the game
    2. If landing on an empty square nothing happens
    3. if landing on a conversion square save piece type for available later
2. opponent move 
    1. If landing on the barian game over
    2. if landing on an empty space look for check and warn if needed.
    

Things that need fixing/next steps <br>
- give the barbarian some space at start (only if possible)
- 
