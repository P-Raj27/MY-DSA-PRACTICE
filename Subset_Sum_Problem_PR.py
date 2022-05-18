def canPartition(nums) -> bool:
        print("HI")
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s//2
        partialSums = set([0])
        count=0
        for num in nums:
            
            for s in list(partialSums):
                
                if num + s == target:
                    
                    count=count+1
                    return True
                partialSums.add(s + num)
        print(partialSums)
        print("count=",count)
        return False
print(canPartition([1,2,3]))
