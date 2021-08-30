class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(map.get(nums[i])!=null)
            {
               map.put(nums[i],map.get(nums[i])+1);
            }else{
                 map.put(nums[i],1);
            }
        }
        
        int j=0;
        int temp=0;
        while(j<k){
            int maxValueInMap=(Collections.max(map.values()));
            int data = findelement(map,maxValueInMap);
            res[temp++]=data;
            
            map.remove(data);
            j=j+1;
        }
        
       //System.out.println(map);
        
        return res;
    }
    public int findelement(HashMap<Integer,Integer> map,int maxdata){
        int result=0;
        for(HashMap.Entry<Integer, Integer> entry : map.entrySet()){
            if(entry.getValue()==maxdata){
                result = entry.getKey();
            }
        }
        return result;
    }
}