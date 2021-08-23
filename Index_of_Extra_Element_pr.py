#No additional comments is required as its a simple problem.
#Note:This Solution doesnt align directly with the geeks for geeks inout mechanism,but gives the idea of the solution.
lst1=[int(x) for x in input().split()]
lst2=[int(x) for x in input().split()]
for i in range(max(len(lst1),len(lst2))):
    
    if(i==min(len(lst1),len(lst2))):             #This Condition is used when the extra element is at the last.
        print("i=,",i)
        break
    if(lst1[i]!=lst2[i]):
        print(i)
        break
    
        
