class Solution {
public:
    bool isAnagram(string s, string t) {
        int m=s.size(); int n=t.size();
        if(n!=m)
        return false;
        unordered_map< char,int> s1;
        unordered_map< char,int> s2;
        int count =0;
        for(int i =0; i <m ;i++)
        {
            s1[s[i]]++;
        } 
        for(int i =0; i <m ;i++)
        {
            s2[t[i]]++;
        } 
        for(int i =0;i<m ;i++)
        {
            if(  s1[s[i]] !=  s2[s[i]]  )
            return false;
        }
       
        return true; 
    }  
};
