class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max_lenn=0
        start_idx=-1
        for i in range(len(nums)):
            if nums[i]>threshold:
                start_idx=-1
            elif start_idx==-1 and nums[i]%2==0:
                start_idx=i

            elif i>0 and nums[i]%2==nums[i-1]%2:
                start_idx=i if nums[i]%2==0 else -1
            if start_idx!=-1:
                max_lenn=max(max_lenn,i-start_idx+1)


        return max_lenn
