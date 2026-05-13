class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set <int> s;
        if (nums.size()<2)
        {
            return false;
        }
        else 
        for(int num : nums)
        {
            if (s.count(num))
            {
                return true;
            }
            s.insert(num);
        }
        return false;
    }};
