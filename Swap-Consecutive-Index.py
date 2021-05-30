class Solution:
   def solve(self, nums):
      length = len(nums)
      for i in range(0,length,4):
         if(i+2<length):
            nums[i], nums[i+2] = nums[i+2], nums[i]
         if(i+3<length):
            nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
      return nums