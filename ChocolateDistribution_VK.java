class Solution
{
    public long findMinDiff (ArrayList<Long> a, long n, long m)
    {
       // Arrays.sort(a);
        Collections.sort(a);
        //System.out.println(a);
        long min = 1000000000;
        for(int i=0;i<=n-m+1;i++){
            if(a.get(m-1+i)<min){
                min = (long)a.get(m-1+i)-(long)a.get(i);
            }
        }
        
        return min;
    }
}