class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> sol;
        unordered_map<string, int> anagrams;
        int index = 0;
        for(int i = 0; i < strs.size(); i++){
            string sortedString = strs[i];
            sort(sortedString.begin(), sortedString.end());
            if(anagrams.count(sortedString) == 0){
                vector<string> newAnagram = {strs[i]};
                anagrams[sortedString] = index;
                sol.push_back(newAnagram);
                index++;
            } 
            else
            {
                sol[anagrams[sortedString]].push_back(strs[i]);
            }
        }
        return sol;
    }
};
