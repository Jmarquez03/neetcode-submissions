class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize the dictonary num : count
        count = {}
        # Initialize the bucket list where the index is the count and the value in the index is the numbers that have that count. 
        bucket = [[] for i in range(len(nums) + 1)]

        # Populate the count dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # Populate the bucket list
        for num, cnt in count.items():
            bucket[cnt].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res