#Using Backtracking
def helper(string,n,vowels,start):
    if(n==0):
        lst.append(string)
        return
    for i in range(start,len(vowels)):
        helper(string+vowels[i],n-1,vowels,i)
if __name__=="__main__":
    n=33
    vowels=["a","e","i","o","u"]
    string=""
    start=0
    lst=[]
    helper(string,n,vowels,start)
    print(len(lst))
