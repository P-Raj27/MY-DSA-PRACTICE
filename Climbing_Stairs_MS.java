class Solution {
    public int climbStairs(int n) {
        
        if(n<=2)
            return n;
        
        int x = 1;
        int y = 2;
        int sum = 0;
        for(int i=3;i<=n;i++)
        {
            sum = x+y;
            x = y;
            y = sum;
        }
        return sum;
        
    }
}