#String Permutation using Recursion.
def permutation(string,final_list):
    lst=[]
    if(len(string)==1):
        return [string]
    else:
        for i in range(len(string)):
            temp_string=string[:i]+string[i+1:]
            lst=[string[i]+x for x in permutation(temp_string,final_list)]
            final_list=final_list+lst
    #print(lst)
    return final_list
    
if __name__=="__main__":
    string=input()
    final_list=[]
    string=sorted(list(string))
    string_sorted=""
    for i in string:
        string_sorted=string_sorted+i
    lst=permutation(string_sorted,final_list)
    #print(lst)
    list_of=[]
    for i in lst:
        if(len(i)==len(string)):
            list_of.append(i)
    print(list_of)
