class Solution {
public:
    bool isPalindrome(string s) {
        // convert to lowercase
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        
        int length = s.length();
        int l = 0;
        int r = length - 1;
    
        // loop through string, use two pointer
        for (int i = 0; i < length; i++) {
            // if s[l] non alphanum, go to next char
            if (!isalnum(s[l])) l++;
            
            // if s[r] non alphanum, go to next char
            else if (!isalnum(s[r])) r--;
            
            // if both chars are good, compare if same. if so, move both pointers
            else if (s[l] == s[r]) {
                l++;
                r--;
            }
            
            // if different, not palindrome
            else return false;
        }
        
        return true;
    }
};