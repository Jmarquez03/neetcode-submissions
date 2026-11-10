class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initialize a dictionary with the number : count
        count = {}
        #buckets where the numbers will be put in the index of their count.
        bucket = [[] for i in range(len(nums) + 1)]
        for num in nums:
            # Fill the dictionary with the appropriate values and their count
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            bucket[cnt].append(num)
        # our return list
        res = []
        # len(bucket) - 1 is the last index of the list
        # Until we reach 0 (the first index), we want to decrement an index
        for i in range(len(bucket) - 1, 0, -1):
            # Add every number in that index to the result. 
            for num in bucket[i]:
                res.append(num)
                # In case we have multiple values in with the same frequency and the cutoff is reached, we want to return the answer. 
                if len (res) == k:
                    return res
