#Trying lightest stone withhout Priority Queue..
array=[2,2]
while(len(array)>1):
    array.sort()
    bigger=array.pop()
    smaller=array.pop()
    if(bigger==smaller):
        continue
    else:
        array.append(bigger-smaller)
print(array[0])
#Conversly you can use PPriorty Queue also.
  
