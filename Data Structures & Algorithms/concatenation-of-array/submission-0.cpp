class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int>n =nums;
        n.insert(n.end(),nums.begin(),nums.end());
        return n;

        
    }
};