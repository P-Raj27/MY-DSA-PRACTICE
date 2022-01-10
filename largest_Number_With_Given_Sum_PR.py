def largestNum(self,N,S):
        
        # code here
        #N=int(input())
        #S=int(input())
        number=""
        if(S > 9*N):
            return (-1)
        elif(S>9):
    #number=number+"9"
            for i in range(N):
        
                if(S>=9):
                    S=S-9
                    number=number+"9"
                elif(S<9):
                    number=number+str(S)
                    S=0
            return ((number))
        else:
            for i in range(N):
                if(i==0):
                    number=number+str(S)
                else:
                    number=number+"0"
            return ((number))
    
