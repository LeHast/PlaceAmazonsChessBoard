#BY::CEBASTIAN SANTIAGO AND DANIEL
############### CS480 AI Project 1################
#Modified Program about the Queens problem 
#Placement  on a chessboard

###Data Structures Hold Values##
col = set()
dpostive = set()
dneg = set()
nogood  = set()
col_equal = 0
index = 0
final_board = []
vector = []
pregrid  = [[]]
board = []
sec_copy = [[]]
countone = 0
counttwo = 0

#Get the One D Vector to build the board
board = [int(item) for item in input("Enter the placements of the amazons:::Enter input like this -> 1 2 3:: ").split()]

#IF the board is empty its valid 
if(len(board) == 0):
    print("vector is empty ", board)
    print("Expanded nodes",0)
    exit()

#Get the dimension of the board
num = input("Enter the Dimension of the board:: ", )
n  = int(num)

#count the amazons of the original board
for i in range(len(board)):
    if(board[i] != -1):
       countone+=1



##PRINTS A 2D GRID OF THE CHESS BOARDS WHERE WE PLACED###
###THE AMAZONS SIMPLE TWO D VECTOR ######################
def printboard(chess):
    print("Amazons placed on the chessboard")
    for i in range(len(chess)):
        for j in range(len(chess[i])):
            print(chess[i][j],end=' ')
        print()




##Create a board with the given input 
def prebuild(array):
      skip = 0
      ##Loop through the created grid##
      ##skips the row if we have a -1##
      ##if the column index is equal ##
      ##to the array number place the##
      ##Amazon at that row,col once  ##
      ##skip is out of range just    ##
      ##break or cointue till we exit##
      for r in range(len(pregrid)):
          for c in range(len(pregrid[r])):
              if(skip > len(array)-1):
                  break
              if(array[skip] == -1):
                  skip+=1
                  break
              if(array[skip] == c):
                  skip+=1
                  pregrid[r][c] = 'A'
                  break
                            
                
##Function to check where the amazons are at on the board###
##The amazons placed by the user############################
def check(board,c,dn,dp,no):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if(board[r][c] == 'A'):
                #Keep Track of the cols were
                #Amazons Can't be placed
                col.add(c)
                
                #Track the positive diagonal r+c
                #Track the negative diagonal r-c
                dp.add(r+c)
                dn.add(r-c)
                
                #Track the kight moves since it can move in eight 
                #different places eight times
                no.add((r+1,c-2))      
                no.add((r-1,c-2))              
                no.add((r+1,c+2))
                no.add((r-1,c+2))
                no.add((r-2,c+1))
                no.add((r-2,c-1))      
                no.add((r+2,c+1))
                no.add((r+2,c-1))




#Create the board by looping throught the dimension n  and time it by '.'
#Creates the n by n board
pregrid = [["."] * n for i in range(n)]
#Create the board with the initial input##################################
prebuild(board)
check(pregrid,col,dneg,dpostive,nogood)



#Print the input received
def initalboard():
    print()
    print("Initial Board")
    for i in range(len(pregrid)):
        for j in range(len(pregrid[i])):
            print(pregrid[i][j],end=' ')
        print()
    #print the vector 
    print("Vector",board)
    print()

initalboard()



def amazon(chess):
    count = 0
    for r in range(len(chess)):
        for c in range(len(chess[r])):
            if chess[r][c] == 'A':
                count+=1
    return count

##Create DFS#######
def amazondfs(r,idx,cols):
    #1.Base Case
    #once we reach the last length of the board
    if(r == n):
        ##Return the build board with all possible amazons on it
        copy =  ["".join(row) for row in pregrid]
        final_board.append(copy)
        return

    #Loop through the columns of the board
    for c in range(n):
        #If Amazons already placed keep going
        if(board[idx] != -1):
            amazondfs(r+1,idx+1,cols=0)
        
        #check if the column is avaiable to put a Amazon 
        if(c in col or (r+c) in dpostive or (r-c) in dneg or (r,c) in nogood):
            #the if statement to check when we can't place an 
            #amazon within a column
            #The cols just checks when we reach the end of the column
            #Recursion call this function
            cols+=1
            if(cols == n):
                amazondfs(r+1,idx+1,cols=0)
            continue

        #UPDATE Data 
        #If we can add an amazon keep track of it col ,diganally postive and negtive
        #plus keep track of the eight knight moves
        col.add(c)
        dpostive.add(r+c)
        dneg.add(r-c)
        
            
        nogood.add((r+1,c-2))      
        nogood.add((r-1,c-2))
        nogood.add((r+1,c+2))
        nogood.add((r-1,c+2))        
        nogood.add((r-2,c+1))
        nogood.add((r-2,c-1))                  
        nogood.add((r+2,c+1))
        nogood.add((r+2,c-1))

        #place an amazon
        pregrid[r][c] = "A"

        #Recursion call till we hit the last row
        amazondfs(r+1,idx+1,cols=0)

        #clear the stack calls
        col.remove(c)
        dpostive.remove(r+c)
        dneg.remove(r-c)
        pregrid[r][c] = "."
    return final_board




def maximum():
    mins = 0
    maxs = 0
    
    for r in range(len(pregrid)):
      for c in range(len(pregrid)):  
          #check if the column is avaiable to put a Amazon 
          if(c in col or (r+c) in dpostive or (r-c) in dneg or (r,c) in nogood):
              continue
          else:
               if(board[r] != -1):
                   break
               pregrid[r][c] = 'A'
               col.add(c)
               dpostive.add(r+c)
               dneg.add(r-c)
               board[r] = c
            
               nogood.add((r+1,c-2))      
               nogood.add((r-1,c-2))
               nogood.add((r+1,c+2))
               nogood.add((r-1,c+2))        
               nogood.add((r-2,c+1))
               nogood.add((r-2,c-1))                  
               nogood.add((r+2,c+1))
               nogood.add((r+2,c-1))
               amazondfs(0,index,col_equal)

               chess = final_board[0]
               printboard(chess)
               print(amazon(chess))
               final_board.clear()
               chess.clear()
               col.remove(c)
               dpostive.remove(r+c)
               dneg.remove(r-c)
               pregrid[r][c] = '.'
               nogood.clear()
               check(pregrid,col,dneg,dpostive,nogood)     
               board[r] = -1
  
               



#Get the board
boards  = maximum()

print()

##Counts the nodes expanded by DFS##
def nodesexpanded():
    start = len(board)
    count = 0

    for i in boards[start:]:
        count+=1
    #return count + 1 since the intial root node 
    #is level one  + count being the path we took down the search tree
    return count+1


#####Gets passed a 2D Vector######
#####Checks were the Amazons are placed
#####Also checks if there is a -1 on the board
#####If there is a '.' equal to 
#####to the length of the columns we have a -1
#####Creates one D array of the Amazons placed
def appendvector(vec):
    count = 0
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            if(boards[i][j] == 'A'):
                vec.append(j)
                count = 0
            else:
                count+=1
        if(count  == len(boards[i])):
                vec.append(-1)
        count = 0



#appendvector(vector)


#for i in range(len(vector)):
    #if vector[i] != -1:
        #counttwo+=1


##Outputs information about the program to the user##
#if(counttwo >= countone):
        #printboard()
        #print()
        #print()
        #print("Vector::",vector)
        #print("Nodes expanded::", nodesexpanded())

#else:
    #initalboard()
    #print("Vector::",vector)
    #print("Nodes expanded::", nodesexpanded())





