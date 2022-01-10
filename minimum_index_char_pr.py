def printMinIndexChar(self, S, patt):
		#Code here
	#	S=input()
      #  patt=input()
        S_list=list(S)
        minimum=len(S_list)-1
        flag=0
        index=minimum+1
        for i in patt:
            if(i in S_list):
                index=S_list.index(i)
                flag=1
            if(index<minimum):
                minimum=index
        if(flag==0):
            return "$"
        else:
            return (S_list[minimum])
