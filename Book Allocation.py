#using Different Function.

def is_possible(array,students,pages):
    count = 0
    sum_allocated = 0
    for i in range(len(array)):
        if(sum_allocated + array[i] > pages):
            count = count + 1
            sum_allocated = array[i]
            if(sum_allocated > pages):
                return False
        else:
            sum_allocated = sum_allocated + array[i]
    print("count is ",count)
    if (count < students):
        return True
    return False

if __name__ == "__main__":
    
    array = [12,34,67,90]
    students = 2
    low = min(array)
    high = sum(array)
    print("low is",low)
    print("high is",high)
    while(low <= high):
        mid = (high + low)//2
        print("mid is = ",mid,low,high)
        if(is_possible(array,students,mid)):
            high = mid - 1
        else:
            low = mid + 1
    print(low)
    
        
    
