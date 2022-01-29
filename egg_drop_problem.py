k=int(input()) #number of floors
n=int(input()) #number of eggs
array=[[None]*(k+1) for i in range(n+1)]   #2d array
for eggs in range(n+1):
    for floors in range(k+1):
        #print(array)
        if(eggs==0 or floors==0):
            array[eggs][floors]=0
        elif(floors==1):
            array[eggs][floors]=1
        elif(eggs==1):
            array[eggs][floors]=floors
        else:
            max_element_final=1000
            for floor in range(1,floors+1):
                print(f"eggs are={eggs} and floors={floors}")
                egg_break=array[eggs-1][floor-1]
                print("breaking=",eggs-1,floor-1)
                egg_not_break=array[eggs][floors-floor]
                print("not breaking",eggs,floors-floor)
                max_element=max(egg_break,egg_not_break)
                max_element_final=min(max_element_final,max_element)
                print("max_element_final=",max_element_final)
                
                #print(max_element_final)
            array[eggs][floors]=1+max_element_final
print(array[n][k])
print(array)
