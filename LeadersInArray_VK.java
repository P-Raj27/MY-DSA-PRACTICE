class Solution{
    //Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int arr[], int n){
        
        ArrayList<Integer> res = new ArrayList<>();
        res.add(arr[n-1]);
        int max = arr[n-1];
        for(int i=n-2;i>=0;i--){
            if(arr[i]>=max){
                //System.out.println("max"+max);
                res.add(arr[i]);
                max = arr[i];
            }
            
        }
        
        
        Collections.reverse(res);
        
        return res;
    }
    
    
}