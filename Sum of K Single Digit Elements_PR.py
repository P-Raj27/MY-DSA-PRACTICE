#using Backtracking
def helper(path,k,start,target):
    if(k==0 and target==0):
        lst.append(path)
        print(path)
        return
    elif(k==0 or target<=0):
        #print(path)
        return
    for i in range(start,10):
        #print("I am here")
        helper(path+[i],k-1,i+1,target-i)
if __name__=="__main__":
    k=3
    target=9
    start=1
    path=[]
    lst=[]
    helper(path,k,start,target)
    print(lst)
