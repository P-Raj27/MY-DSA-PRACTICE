class Solution{
    //Function to partition the array around the range such 
    //that array is divided into three parts.
    public void threeWayPartition(int array[], int a, int b)
    {
        int start=0;int end=array.length-1;
        for(int i=0;i<=end;){
            if(array[i]<a){
                int temp = array[start];
                array[start] = array[i];
                array[i]=temp;
                start++;
                i++;
            }else if(array[i]>b){
                int temp = array[end];
                array[end] = array[i];
                array[i]=temp;
                end--;
            }else{
                i++;
            }   
        }
    }
}
