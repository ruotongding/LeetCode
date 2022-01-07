# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
#
# 示例 1:
#
# 输入:
# "abccccdd"
#
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindrome

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        n = len(s)
        for i in range(n):
            if s[i] not in dict:
                dict[s[i]]=0
            dict[s[i]]+=1
        n1 = len(dict)
        length=0
        if n1==1:
            for i in dict:
                return dict[i]
        odd = []

        sumnum=0
        oddsum=0
        for i in dict:
            sumnum+=dict[i]
            if dict[i]%2!=0:
                oddsum+=1
        if oddsum>1:
            sumnum = sumnum-oddsum+1

        print(dict)

        return sumnum
