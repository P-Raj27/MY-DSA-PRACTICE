key_map={"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz","0":""}
def combination(output,cr,length,lst,lst2):
    if(cr==length):
        #print(output)
        lst2.append(output)
        return 
    string=key_map[lst[cr]]
    for i in range(len(string)):
        output=output+string[i]
        combination(output,cr+1,length,lst,lst2)
        output=output[0:len(output)-1]
    
if __name__=="__main__":
    lst=[str(x) for x in input().split()]
    output=""
    cr=0
    length=len(lst)
    lst2=[]
    combination(output,cr,length,lst,lst2)
    #print(comb_list)
    print("lst2 is=",lst2)
