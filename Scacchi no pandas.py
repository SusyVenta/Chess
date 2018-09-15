#___chessboard
board = [[[0 for z in range(5)] for y in range(8)] for x in range(8)]

#[y][x][z]
#z: 0= pres piece, 1=owner pres piece, 2= new piece, 3= owner new piece, 4=coordinates
board[0][0][0]="r"
board[0][0][1]=1 #1= blacks

board[0][7][0]="r"
board[0][7][1]=1 

board[7][0][0]="r"
board[7][0][1]=0 #0= whites

board[7][7][0]="r"
board[7][7][1]=0 

board[0][1][0]="k"
board[0][1][1]=1

board[0][6][0]="k"
board[0][6][1]=1

board[7][1][0]="k"
board[7][1][1]=0

board[7][6][0]="k"
board[7][6][1]=0

board[0][2][0]="b"
board[0][2][1]=1

board[0][5][0]="b"
board[0][5][1]=1

board[7][2][0]="b"
board[7][2][1]=0

board[7][5][0]="b"
board[7][5][1]=0

board[0][4][0]="q"
board[0][4][1]=1

board[7][3][0]="q"
board[7][3][1]=0

board[0][3][0]="ki"
board[0][3][1]=1

board[7][4][0]="ki"
board[7][4][1]=0
#__coordinates
board[0][0][4]="a8"
board[1][0][4]="a7"
board[2][0][4]="a6"
board[3][0][4]="a5"
board[4][0][4]="a4"
board[5][0][4]="a3"
board[6][0][4]="a2"
board[7][0][4]="a1"

board[0][1][4]="b8"
board[1][1][4]="b7"
board[2][1][4]="b6"
board[3][1][4]="b5"
board[4][1][4]="b4"
board[5][1][4]="b3"
board[6][1][4]="b2"
board[7][1][4]="b1"

board[0][2][4]="c8"
board[1][2][4]="c7"
board[2][2][4]="c6"
board[3][2][4]="c5"
board[4][2][4]="c4"
board[5][2][4]="c3"
board[6][2][4]="c2"
board[7][2][4]="c1"

board[0][3][4]="d8"
board[1][3][4]="d7"
board[2][3][4]="d6"
board[3][3][4]="d5"
board[4][3][4]="d4"
board[5][3][4]="d3"
board[6][3][4]="d2"
board[7][3][4]="d1"

board[0][4][4]="e8"
board[1][4][4]="e7"
board[2][4][4]="e6"
board[3][4][4]="e5"
board[4][4][4]="e4"
board[5][4][4]="e3"
board[6][4][4]="e2"
board[7][4][4]="e1"

board[0][5][4]="f8"
board[1][5][4]="f7"
board[2][5][4]="f6"
board[3][5][4]="f5"
board[4][5][4]="f4"
board[5][5][4]="f3"
board[6][5][4]="f2"
board[7][5][4]="f1"

board[0][6][4]="g8"
board[1][6][4]="g7"
board[2][6][4]="g6"
board[3][6][4]="g5"
board[4][6][4]="g4"
board[5][6][4]="g3"
board[6][6][4]="g2"
board[7][6][4]="g1"

board[0][7][4]="h8"
board[1][7][4]="h7"
board[2][7][4]="h6"
board[3][7][4]="h5"
board[4][7][4]="h4"
board[5][7][4]="h3"
board[6][7][4]="h2"
board[7][7][4]="h1"

def chessboard():
    chessboard=[[str(z[0])for z in line] for line in board]
    for i in range (8):
        for j in range (8):
            print ((chessboard[i][j]+"   "+(" " if chessboard[i][j]!="ki" else "")),end="",flush=True)
        print ("\n")
chessboard()
def letters_to_num():
        global col_pos
        global tmp_col_pos
        global col_dest
        global tmp_col_dest
        if col_pos=="a":
            tmp_col_pos=1
        elif col_pos=="b":
            tmp_col_pos=2
        elif col_pos=="c":
            tmp_col_pos=3
        elif col_pos=="d":
            tmp_col_pos=4
        elif col_pos=="e":
            tmp_col_pos=5
        elif col_pos=="f":
            tmp_col_pos=6
        elif col_pos=="g":
            tmp_col_pos=7
        elif col_pos=="h":
            tmp_col_pos=8
        if col_dest=="a":
            tmp_col_dest=1
        elif col_dest=="b":
            tmp_col_dest=2
        elif col_dest=="c":
            tmp_col_dest=3
        elif col_dest=="d":
            tmp_col_dest=4
        elif col_dest=="e":
            tmp_col_dest=5
        elif col_dest=="f":
            tmp_col_dest=6
        elif col_dest=="g":
            tmp_col_dest=7
        elif col_dest=="h":
            tmp_col_dest=8

#____pieces functions

def rook (position, destination):
    global board
    global row_pos
    global col_pos
    global row_dest
    global col_dest
    def nums_to_letters():
        nonlocal f_to_check
        nonlocal to_check
        for i in to_check:
            if i[0]=="1":
                f_to_check.append("a"+str(i[1]))
            elif i[0]=="2":
                f_to_check.append("b"+str(i[1]))
            elif i[0][0]=="3":
                f_to_check.append("c"+str(i[1]))
            elif i[0]=="4":
                f_to_check.append("d"+str(i[1]))
            elif i[0]=="5":
                f_to_check.append("e"+str(i[1]))
            elif i[0]=="6":
                f_to_check.append("f"+str(i[1]))
            elif i[0]=="7":
                f_to_check.append("g"+str(i[1]))
            elif i[0]=="8":
                f_to_check.append("h"+str(i[1]))
    #check if piece selected is in position
    for line in board:
        for z in line:
            if z[4]==position:
                if z[0]=="r":
                    #check if move is possible
                    if col_pos==col_dest and row_pos!=row_dest: #checks that it moves only vertically
                        to_check=[]
                        diff=abs(int(row_dest)-int(row_pos))
                        count=1
                        if int(row_dest)>int(row_pos): #checks that it moves upward
                            for i in range (diff):
                                to_check.append(col_pos+str(int(row_pos)+count))
                                count+=1
                        else:#checks that it moves downward
                            for i in range (diff):
                                to_check.append(col_pos+str(int(row_pos)-count))
                                count+=1
                        #checks that there are no pieces inbetween position and destination
                        for line in board:
                            for z in line:
                                for i in to_check:
                                    if z[4]==i:
                                        if z[0]==0:
                                            return True
                                        else:
                                            return "Invalid move"
                    elif row_pos==row_dest and col_pos!=col_dest:#checks that it moves only horizontally
                        letters_to_num()
                        diff= abs(int(tmp_col_dest)-int(tmp_col_pos))
                        to_check=[]
                        count=1
                        if tmp_col_dest>tmp_col_pos:
                            for i in range (diff):
                                to_check.append(str(tmp_col_pos+count)+ row_pos)
                                count+=1
                        else:
                            for i in range (diff):
                                to_check.append(str(tmp_col_pos-count)+row_pos)
                                count+=1
                        f_to_check=[]
                        nums_to_letters()
                        #checks that there are no pieces inbetween position and destination
                        for line in board:
                            for z in line:
                                for i in f_to_check:
                                    if z[4]==i:
                                        if z[0]==0:
                                            return True
                                        else:
                                            return "Invalid move"

                    else:
                        return "Invalid move"
                else:
                    return "There is no rook in that position"

def knight (position, destination):
    global board
    global row_pos
    global col_pos
    global row_dest
    global col_dest
    global tmp_col_pos
    global tmp_col_dest
    #check if piece selected is in position
    for line in board:
        for z in line:
            if z[4]==position:
                if z[0]=="k":
                #check if move is possible
                    letters_to_num()
                    #moves as T upward(l\r)
                    if int(row_dest)==int(row_pos)+2 and (int(tmp_col_dest)==int(tmp_col_pos)-1 or int(tmp_col_dest)==int(tmp_col_pos)+1):
                        return True
                    #moves as T downward(l\r)
                    elif int(row_dest)==int(row_pos)-2 and (int(tmp_col_dest)==int(tmp_col_pos)-1 or int(tmp_col_dest)==int(tmp_col_pos)+1):
                        return True
                    #moves as --|
                    elif int(tmp_col_dest)==int(tmp_col_pos)+2 and (int(row_dest)==int(row_pos)-1 or int(row_dest)==int(row_pos)+1):
                        return True
                    #moves as |--
                    elif int(tmp_col_dest)==int(tmp_col_pos)-2 and (int(row_dest)==int(row_pos)-1 or int(row_dest)==int(row_pos)+1):
                        return True
                    else:
                        return "Invalid move"
                else:
                    print ("There is no knight in that position")
                    return 0
def bishop(position, destination):
    global board
    global row_pos
    global col_pos
    global row_dest
    global col_dest
    global tmp_col_pos
    global tmp_col_dest
    #check if piece selected is in position
    for line in board:
        for z in line:
            if z[4]==position:
                print ("position")
                if z[0]=="b":
                    print ("z[0]=b")
                    letters_to_num()
                #check if move is possible
                    x=abs(int(tmp_col_dest)-int(tmp_col_pos))
                    if abs(int(tmp_col_dest)-int(tmp_col_pos))==abs(int(row_dest)-int(row_pos)) and 1<=x<=7:
                        count=1
                        to_check=[]
                        if int(row_dest)>(row_pos) and int(tmp_col_dest)>int(tmp_col_pos):
                            for i in x:
                                to_check.append(str(int(row_pos+count))+str(int(tmp_col_pos+count)))
                                if to_check!=None:
                                    return True
                            print (to_check)
                                
                        


                    
            else:
                print ("There is no bishop in that position")
                return 0
                    

#___game
def move():
    global board
    global coords_ptm
    global destination
    global only_piece
    #delete piece and owner from old position
    for line in board:
        for z in line:
            if z[4]==coords_ptm:
                z[0]=0
                z[1]=0
            elif z[4]==destination:#put piece in new position
                if (turn ==0 and z[1]==1)or (turn==1 and z[1]==0):
                    z[0]=only_piece
                    z[1]=(0 if turn==0 else 1)
                else:
                    return "You can't take your own pieces!"
                
count=1
def check_mate():
    turn=10
while not check_mate():
    if count%2==0:
        turn=1
    else:
        turn=0
    piece_to_move=input("What piece do you want to move, %s?\nExample: rook a2 (a2 is the piece's current position)\n"%("player 1" if turn==0 else "player 2"))
    destination=input("Where do you want to move it?\n Example: a4 (a4 is the piece's destination)\n")
    piece_to_move=piece_to_move.split(" ")
    only_piece=str(piece_to_move[0])
    coords_ptm=str(piece_to_move[1])
    col_pos=str(coords_ptm[0])
    col_dest=str(destination[0])
    row_pos=str(coords_ptm[1])
    row_dest=str(destination[1])

    if only_piece=="r":
        if rook(coords_ptm, destination):
            if move():
                count+=1
                chessboard()   
        else:
            print ("Invalid move: try again")
    elif only_piece=="k":
        if knight(coords_ptm, destination):
            move()
            count+=1
            chessboard()
        else:
            print ("Invalid move: try again")
    elif only_piece=="b":
        if bishop(coords_ptm, destination):
            move()
            count+=1
            chessboard()
        else:
            print ("Invalid move: try again")


















