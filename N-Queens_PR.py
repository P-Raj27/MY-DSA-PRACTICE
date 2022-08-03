#N queens.

def helper(col,leftRow,lowerDiagonal,upperDiagonal,board,ans,n,temp_res):
    
    if(col == n):
        temp_res = []
        for row in board:
                temp_res.append("".join(row))
        ans.append(temp_res)
        print(f"answer is temp= {temp_res}")
        return
        #print(board)
        #print(leftRow)
    else:
        for i in range(0,n):
            if(leftRow[i] == 0 and lowerDiagonal[i+col] == 0 and upperDiagonal[n-1+col-i] == 0):
                
                #print(f"for i ={i} and col = {col}")
                #print("before any changes board = ",board)
                leftRow[i] = 1
                lowerDiagonal[i+col] = 1
                upperDiagonal[n-1+col-i] = 1
                board[i][col] = "Q"
                #print(f"when i = ={i}")
                #print("board is =",board)
                helper(col+1,leftRow,lowerDiagonal,upperDiagonal,board,ans,n,temp_res)
                board[i][col] = "."
                #print("board is =",board)
                leftRow[i] = 0
                #temp_res.pop()
                lowerDiagonal[i+col] = 0
                upperDiagonal[n-1+col-i] = 0
                
                
                
                
    
    
    
if __name__ == "__main__":
    
        n = 4
        row = ["." for x in range(n)]
            #for i in range (n):
            #   string = string + "."
        board = [["." for x in range(n)] for x in range(n)]
        print(board)
        ans = []
        leftRow = [0 for x in range(n)]
        lowerDiagonal = [0 for x in range((2*n)-1)]
        upperDiagonal = [0 for x in range((2*n)-1)]
        col = 0
        temp_res = []
        helper (col,leftRow,lowerDiagonal,upperDiagonal,board,ans,n,temp_res)
        print("answer is = ",ans)
