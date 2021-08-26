class Solution
{
    public:
    void sort012(int v[], int n)
    {
         
        int low=0;
        int high=n-1;
        int mid=0;
        
        while(mid<=high)
        {
            switch(v[mid])
            {
                case 0:
                {
                    swap(v[mid],v[low]);
                    mid++;
                    low++;
                    break;
                }
                
                case 1:
                {
                    mid++;
                    break;
                    
                }
                
                case 2:
                {
                    swap(v[mid],v[high]);
                    high--;
                    break;
                }
                
                
            }
        
            
        }
    }
        
    
};

// { Driver Code Starts.
int main() {

    int t;
    cin >> t;

    while(t--){
        int n;
        cin >>n;
        int a[n];
        for(int i=0;i<n;i++){
            cin >> a[i];
        }

        Solution ob;
        ob.sort012(a, n);

        for(int i=0;i<n;i++){
            cout << a[i]  << " ";
        }

        cout << endl;
        
        
    }
    return 0;
}

  // } Driver Code Ends


