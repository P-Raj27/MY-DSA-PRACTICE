class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = []

        op = ['[','{','(']
        cl = [']','}',')']
        dic = {']':'[','}':'{',')':'('}
        
        
        for brac in list(x):
          if brac in op:
            stack.append(brac)
            
          elif brac in cl: 
            idx = cl.index(brac)
            if (len(stack)>0) and (op[idx]==stack[len(stack)-1]):
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return(True)
        else:
            return False
