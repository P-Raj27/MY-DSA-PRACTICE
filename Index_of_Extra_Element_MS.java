// { Driver Code Starts
import java.util.*;
class ExtraElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] a = new int[n];
            int[] b = new int[n - 1];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            for (int i = 0; i < n - 1; i++) b[i] = sc.nextInt();
            Solution g = new Solution();
            System.out.println(g.findExtra(a, b, n));
        }
    }
}// } Driver Code Ends


/*Complete the function below*/
class Solution {
    
    
    public int findExtra(int a[], int b[], int n) {
        // add code here.
        if(a[0]!=b[0])
            return 0;
        int low = 0;
        int high = n-1;
        while(low<high)
        {
            int mid = (low+high)/2;
            if(a[mid] == b[mid])
                low = mid;
            else
                high = mid;
            if(low == high-1)
                break;
        }
        return high;
    }
}