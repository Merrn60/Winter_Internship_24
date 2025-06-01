class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set() #unique values only
        mark=0
        for num in range(len(nums)-1): #trace number in list
         mark = nums[num] +nums[num+1] #sum each 2 consecutive number
         if mark in seen: #3la tool return true if seen
             return True
         seen.add(mark)
        return False # if nope return false