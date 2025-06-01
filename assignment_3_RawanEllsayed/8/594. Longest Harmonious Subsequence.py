class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=Counter(nums)
        max_len=0
        for i in freq:
            if i+1 in freq:
                max_len = max(max_len,freq[i]+freq[i+1])
        return max_len
