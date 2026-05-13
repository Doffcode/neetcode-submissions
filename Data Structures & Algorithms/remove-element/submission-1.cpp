class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count =0;
        int n = nums.size();
        int count_array[n]={0};
        for (int i = 0; i<n; i++)
        {
            if (nums[i]==val)
            count ++;
            count_array[i]=count;
        }
        for(int i=0; i<n; i++)
        {
            if(nums[i]!=val)
            {
                nums[i-count_array[i]]=nums[i];
            }
        }
        return n-count;
    }
};