class Solution {
    public int findExtra(int a[], int b[], int n) {
        int count=0;
        for(int i=0;i<b.length;i++){
            if(a[i]!=b[i]){
                count++;
                //System.out.println(a[i] +" "+b[i]);
                return i;
            }
        }
        if(count==0){
            return a.length-1;
        }
        return n;
    }
}