def isPanagram(self, string):
		# code here
		#string=input().lower().replace(" ","").replace(",","")
		string=string.lower().replace(" ","").replace(",","")
        alphabets="abcdefghijklmnopqrstuvwxyz"
        dictionary={}
        for i in alphabets:
            dictionary[i]=dictionary.get(i,0)
        #print(dictionary)
        for i in string:
            if(i in alphabets):
                
                dictionary[i]=dictionary[i]+1
        flag=0
        for i in dictionary.values():
            if(i==0):
                flag=1
                break
        if(flag==0):
            return ("1")
        else:
            return ("0")
