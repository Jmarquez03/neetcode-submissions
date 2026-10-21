class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
       std::unordered_set<int> numSet;
       for(int i = 0; i < nums.size(); i++){
        if(numSet.count(nums[i]) != 0){
            return true;     
        }
        numSet.insert(nums[i]);
       }
        return false;
    }
};