# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 示例 1:
#
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 示例 2:
#
# 输入: rowIndex = 0
# 输出: [1]
# 示例 3:
#
# 输入: rowIndex = 1
# 输出: [1,1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle-ii


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = rowIndex+1
        if row==1:
            return[1]
        elif row==2:
            return [1,1]

        else:
            line = [1,1]
            for i in range(2,row):
                l = []

                for j in range(len(line)-1):
                    l.append(line[j]+line[j+1])
                line = [1]+l+[1]
                if i == rowIndex:
                    return line
