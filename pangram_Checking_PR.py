def checkPangram(self,s):
        #code here
        alphabets="abcdefghijklmnopqrstuvwxyz"
        #string=input()
        s=s.lower()
        flag=0
        if(len(s)<26):
            return 0
        else:
    
            for i in alphabets:
                if(i not in s):
                 #print(i)
                    flag=1
                    break
    
        if(flag==0):
            return 1
        else:
            return 0
