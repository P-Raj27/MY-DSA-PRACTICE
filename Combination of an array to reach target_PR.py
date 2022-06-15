#Combinations in an array to reach a target
def helper(index,target,comb,ans):
    #print(ans)
    if(index==len(array)):
        if(target==0):
            #print(comb)
            print("ans before",ans)
            print("comb is",comb)
            ans.append(comb)
            return(ans)
        return
    else:
        if(target>=array[index]):
            #picking the element
            comb.append(array[index])
            helper(index,target-array[index],comb,ans)
            comb.pop(-1)
        #Not picking the element
        helper(index+1,target,comb,ans)
if __name__ == "__main__":
    array=[2,3,6,7]
    ans=[]
    comb=[]
    target=7
    print(helper(0,target,comb,ans))
    #print(helper)
    
 
