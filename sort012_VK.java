class Solution
{
    public static void sort012(int a[], int n)
    {
        int low = 0;
        int high = a.length-1;
        int mid = 0;
        
        while(mid<=high){
            switch(a[mid]){
                case 0:
                    int swap = a[low];
                    a[low] = a[mid];
                    a[mid] = swap;
                    low++;
                    mid++;
                    break;
                case 1:
                    mid++;
                    break;
                case 2:
                    int temp = a[mid];
                    a[mid] = a[high];
                    a[high] = temp;
                    high--;
                    break;
            }
        }
        
    }
}