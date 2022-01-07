# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums)<3:
            return []
        a = []
        for i in range(0,len(nums)):
            if nums[i]>0:
                return a
            if (i>0 and nums[i]==nums[i-1]):
                continue
            first = i
            second = i+1
            third = len(nums)-1
            while second<third:
                if nums[first]+nums[second]+nums[third]==0:
                    a.append([nums[first],nums[second],nums[third]])
                    while(second<third and nums[second]==nums[second+1]):
                        second = second+1
                    while(second<third and nums[third]==nums[third-1]):
                        third = third-1
                    second = second+1
                    third = third-1

                elif nums[first]+nums[second]+nums[third]<0:
                    second=second+1
                elif nums[first]+nums[second]+nums[third]>0:
                    third = third-1
        return(a)
