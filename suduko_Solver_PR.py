#Suduko Solver.

def solver(board):
    
    """This Function Traverse from each cell in the board and find the empty slot and then try to fill that slot with number 1-9 
    and check the validity of the number"""
    
    for row in range(len(board)):
        for column in range(len(board[0])):
            
            if(board[row][column] == "."):            #To check if a cell is empty so that we can fill it.
                
                for num in range(1,10):
                    
                    if(isValid(board,row,column,num) == True):      #Checks the Validity of the number based on the suduko Rules
                        board[row][column] = str(num)
                        
                        if(solver(board) == True):       #After filling the cell we check if its compatible with other cell fillings
                            return True
                        else:
                            board[row][column]="."        #If its not compatible then we remove the filled number and try again with another number
                return False
    return True

def isValid(board,row,column,num):
    """This number check the Validity of the value """
    
    num = str(num)
    for i in range(0,9):
        
        if (board[i][column] == num):         #This is the algo to check the validity in the current column
            return False
        elif (board[row][i] == num):          #This is the algo to check the validity in the current row
            return False
        elif (board[3*(row//3)+i//3][3*(column//3)+i%3] == num):       #This is the algo to check in the sub_grid of 3 by 3
            return False
    return True

if __name__ == "__main__":
    
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    
    for i in range(0,9):
        print(board[i])
    solver(board)
    
    #print(board)
    print("-----------------------After Solving the Suduko------------------------------------")
    print()
    print()
    for i in range(0,9):
        print(board[i])
    
