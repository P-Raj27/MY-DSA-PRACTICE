// { Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class Geeks
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int n =sc.nextInt();
            int arr[] = new int[n];
            
            for(int i = 0; i < n; i++)
             arr[i] = sc.nextInt();
             
           System.out.println(new Solution().majorityElement(arr, n)); 
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    static int majorityElement(int arr[], int size)
    {
        // your code here
        HashMap<Integer, Integer> mp = new HashMap<Integer, Integer>();
        for(int i=0;i<size;i++)
        {
            Integer n = mp.get(arr[i]);
            if(n==null)
            {
                mp.put(arr[i], 1);
            }
            else
            {
                mp.put(arr[i], n+1);
            }
        }
        int ans=0;
        for(int i=0;i<size;i++)
        {
            Integer k = mp.get(arr[i]);
            if(k>(size/2))
            {
                ans = arr[i];
                break;
            }
            else
                ans=-1;
        }
        return ans;
    }
}