// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
		    System.out.println(new Solution().evaluatePostFix(br.readLine().trim()));
		}
	}
}// } Driver Code Ends


class Solution
{
    //Function to evaluate a postfix expression.
    public static int evaluatePostFix(String S)
    {
        // Your code here
        Stack<Integer> st = new Stack<Integer>();
        for(int i=0;i<S.length();i++)
        {
            char ch = S.charAt(i);
            //System.out.println(ch);
            if(ch>='0' && ch<='9')
            {
                st.push(Character.getNumericValue(ch));
            }
            if(ch=='+' && !st.empty())
            {
                int a = st.pop();
                int b = st.pop();
                int ans = b+a;
                st.push(ans);
            }
            if(ch=='-' && !st.empty())
            {
                int a = st.pop();
                int b = st.pop();
                int ans = b-a;
                st.push(ans);
            }
            if(ch=='*' && !st.empty())
            {
                int a = st.pop();
                int b = st.pop();
                int ans = b*a;
                st.push(ans);
            }
            if(ch=='/' && !st.empty())
            {
                int a = st.pop();
                int b = st.pop();
                int ans = b/a;
                st.push(ans);
            }
        }
        int ans=0;
        if(!st.empty())
        {
            //System.out.println("Hello"+st.peek());
            ans = st.pop();
        }
        return ans;
    }
}