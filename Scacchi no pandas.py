

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
                    
















