import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
    
        if (s.length() <=1) return false;
        
        for (char c : s.toCharArray()) {
            
            if (c == '(') st.push(')');
            
            else if (c == '[') st.push(']');
            
            else if (c == '{') st.push('}');
    
            else if (st.empty() || st.pop() != c) return false;
            
        }
        
        return st.empty();
    }
}