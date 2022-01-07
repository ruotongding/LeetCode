# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subarray-sum-equals-k


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0



        hash = {}
        sum = 0
        count=0
        hash[0]=1
        for i in range(n):
            sum+=nums[i]
            if sum-k in hash:
                count+=hash[sum-k]
            if sum not in hash:
                hash[sum]=0
            hash[sum]+=1
        print(hash)
        return count
