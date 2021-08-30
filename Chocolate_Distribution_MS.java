// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main (String[] args)
    {
        
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            long n = sc.nextLong();
            ArrayList<Long> arr = new ArrayList<Long>();
            for(int i = 0;i<n;i++)
                {
                    long x = sc.nextInt();
                    arr.add(x);
                }
            long m = sc.nextLong();
            
            Solution ob = new Solution();
            
    		System.out.println(ob.findMinDiff(arr,n,m));
        }
        
    }
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    public long findMinDiff (ArrayList<Long> a, long n, long m)
    {
        // your code here
        Collections.sort(a);
        long minsum=0, orgsum=0;
        minsum = a.get((int)m-1) - a.get(0);
        //orgsum = minsum;
        for(int i=0;i<=n-m;i++)
        {
            minsum = Math.min((long)(a.get((int)(i+m-1))) - (long)(a.get(i)), minsum);
            //minsum = Math.min(minsum, orgsum);
        }
        
        return minsum;
    }
}