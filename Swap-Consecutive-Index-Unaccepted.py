class Solution:
    def solve(self, nums):
        visited = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (i % 2 == 0) and (j % 2 == 0) and i not in visited and j not in visited:
                    nums[i], nums[j] = nums[j], nums[i]
                    visited.append(i)
                    visited.append(j)
                elif (i % 2 != 0) and (j % 2 != 0) and i not in visited and j not in visited:
                    nums[i], nums[j] = nums[j], nums[i]
                    visited.append(i)
                    visited.append(j)
        return nums