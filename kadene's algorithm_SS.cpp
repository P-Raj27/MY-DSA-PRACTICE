
// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
    public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(int arr[], int n)
    {
        int max_sum=INT_MIN;
        int currsum=0;
        
        for(int i=0;i<n;i++)
        {
            currsum += arr[i];
            
            if(currsum>max_sum)
            {
                max_sum=currsum;
                
                if(currsum<0)
                currsum=0;
            
            }
            
            else 
            {
                if(currsum<0)
                currsum=0;
                
            }
          
            
           
        }
        
        
        return max_sum;

        
    }
};

// { Driver Code Starts.

int main()
{
    int t,n;
    
    cin>>t; //input testcases
    while(t--) //while testcases exist
    {
        
        cin>>n; //input size of array
        
        int a[n];
        
        for(int i=0;i<n;i++)
            cin>>a[i]; //inputting elements of array
            
        Solution ob;
        
        cout << ob.maxSubarraySum(a, n) << endl;
    }
}
  // } Driver Code Ends











