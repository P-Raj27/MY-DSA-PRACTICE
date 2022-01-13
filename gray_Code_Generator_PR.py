#GrayCodeConverter
#BinaryGeneratorTillN
def corrector(string,num):
    if(len(string)<num):
        for i in range(num-len(string)):
            string="0"+string
    return string
        
def greyGenerator(binary_list,num):
    gray_list=[]
    for i in binary_list:
        string=""
        i=corrector(i,num)
        
        for j in range(len(i)):
            if(j==0):
                string=string+i[j]
            else:
                string=string+str(int(i[j-1])^int(i[j]))
        gray_list.append(string)
    return gray_list
                
            
        
        
def binaryGenerator(num):
    num=2**num
    binary_list=[]
    for i in range(num):
        binary_list.append(bin(i)[2:])
    return binary_list
num=int(input())
binary_list=binaryGenerator(num)
print(binary_list)
gray_list=greyGenerator(binary_list,num)
print(gray_list)


#NOW USING REURSION to Solve.
#Grey Code Generator using recursion
def code_generator(num):
    if(num==1):
        return [0,1]
    l1=code_generator(num-1)
    l2=l1[::-1]
    for i in range(len(l1)):
        l1[i]="0"+str(l1[i])
    for i in range(len(l2)):
        l2[i]="1"+str(l2[i])
    return l1+l2
print(code_generator(2))
        
