class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size()<2)
        {
            return false;
        }
        else 
        return unordered_set <int>(nums.begin(), nums.end()).size() < nums.size(); 
    }};
