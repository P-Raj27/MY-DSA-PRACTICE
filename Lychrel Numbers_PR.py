def isPalindrome(string):
    string=str(string)
    if(string==string[::-1]):
        return True
count=0
array=[False]*1000000
#print(array)
for i in range(1,10000):
    j=0
    flag=0
    while(j<50):
        j=j+1
        number=i+int(str(i)[::-1])
        #print("Number is",number)
        #if(array[number]==True):
         #   flag=1
          #  break
        if(isPalindrome(number)):
            #array[i]=True
            flag=1
            break
        i=number
    if(flag==0):
        #print(i)
        count=count+1
print(count)
