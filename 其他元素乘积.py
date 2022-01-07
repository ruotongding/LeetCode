# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        n = len(nums)
        l = [0]*n
        r = [0]*n
        l[0]=1
        for i in range(1,n):
            l[i]=nums[i-1]*l[i-1]
        r[n-1]=1
        for i in range(n-2,-1,-1):
            r[i]=nums[i+1]*r[i+1]
        for i in range(n):
            b = l[i]*r[i]
            a.append(b)

        return(a)
