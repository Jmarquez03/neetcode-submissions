class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sol;
        unordered_map<int, int> indexMap;
        for(int i = 0; i < nums.size(); i++){
            int search = target - nums[i];
            if(indexMap.count(search) == 0){
                indexMap[nums[i]] = i;
            } else {
                sol.push_back(indexMap[search]);
                sol.push_back(i);
                return sol;
            }
        }
        return sol;
    }
};
