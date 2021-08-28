// solved over leetcode-> same intuition as of kadence's algorithm

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k)
    {
        int currsum=0;
        int count=0;
        int max_sum=INT_MIN;
        double result;
        
        
        int i=0;
        
        while(i<nums.size())
        {
            count++;
            
            currsum += nums[i];
            
            if(count==k)
            {
                if(currsum>max_sum)
                    max_sum=currsum;
                
                currsum -= nums[i-k+1];
                count--;
 
            
            }
            
            i++;
        }
        
        result=(double)max_sum/k;
        
        
        return result;
        
        
        
    }
};
