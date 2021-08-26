
// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

int maxLen(int A[], int n);

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int A[N];
        for (int i = 0; i < N; i++)
            cin >> A[i];
        cout << maxLen(A, N) << endl;
    }
}
// } Driver Code Ends


/*You are required to complete this function*/

int maxLen(int A[], int n)
{
    unordered_map<long,int> m;
    long currsum=0;
    int max_length=0;
    
    for(int i=0;i<n;i++)
    {
        currsum +=A[i];
        
        if(currsum==0)
        {
            if(i+1>max_length)
            max_length=i+1;
            
        }        
            
            else if(m.find(currsum)!=m.end())
            {
                if(i-m[currsum]>max_length)
                max_length=i-m[currsum];
                
            }
            
            else
            {
                m[currsum]=i;
            }
         
            
        }
        
        
    
    
    return max_length;

}


