def minIndexChar(self,string, patt): 
        #code here
        #Have to Create a Hash 
        #string=input()
        #patt=input()
        string_dictionary={}
        minimum=len(string)
        flag=0
        for i in range(len(string)):
            string_dictionary[string[i]]=min(string_dictionary.get(string[i],len(string)-1),i)
        #print (string_dictionary)

        for i in patt:
            value=string_dictionary.get(i,len(string))
            if(value<minimum):
                flag=1
                minimum=string_dictionary[i]
        if(flag==0):
            return ("-1")
        else:
            return (minimum)
            
