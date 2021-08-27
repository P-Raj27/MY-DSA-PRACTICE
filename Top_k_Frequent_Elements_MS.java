// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = Integer.parseInt(s[i + 1]);
            }
            int k = Integer.parseInt(br.readLine().trim());
            Solution obj = new Solution();
            int[] ans = obj.topK(nums, k);
            for (int i = 0; i < ans.length; i++) System.out.print(ans[i] + " ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


class Solution {
    
    public static int[] sortByValue(Map<Integer, Integer> hm, int k)
    {
        List<Map.Entry<Integer, Integer> > list =
               new LinkedList<Map.Entry<Integer, Integer> >(hm.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer> >() {
            public int compare(Map.Entry<Integer, Integer> o1,
                               Map.Entry<Integer, Integer> o2)
            {
                return (o1.getValue()).compareTo(o2.getValue());
            }
        });
        Collections.reverse(list);
        HashMap<Integer, Integer> temp = new LinkedHashMap<Integer, Integer>();
        for (Map.Entry<Integer, Integer> aa : list) {
            temp.put(aa.getKey(), aa.getValue());
        }
        int arr[] = new int[k];
        for(int i=0;i<k;i++)
        {
            arr[i] = list.get(i).getKey();
        }
        return arr;
    }
    
    public int[] topK(int[] nums, int k) {
        // Code here
        HashMap<Integer, Integer> mp = new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++)
        {
            Integer n = mp.get(nums[i]);
            if(n==null)
            {
                mp.put(nums[i], 1);
            }
            else
            {
                mp.put(nums[i], n+1);
            }
        }
        //System.out.println(mp);
        //Map<Integer, Integer> revsortkey = new TreeMap<Integer, Integer>(Collections.reverseOrder());
        //revsortkey.putAll(mp);
        int arr1[] = sortByValue(mp, k);
        //System.out.println(revsortkey);
        //System.out.println(revsortval);
        //Integer arr[] = new Integer[k];
        //arr = revsortval.keySet().toArray();
        
        return arr1;
    }
}