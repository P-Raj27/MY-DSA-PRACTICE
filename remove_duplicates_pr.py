def removeDups(self, S):
		# code here
		#string=input()
        lst=[]
        string1=""

        for i in S:
            if(i not in lst):
                lst.append(i)
        for i in lst:
            string1=string1+i
        return (string1)
