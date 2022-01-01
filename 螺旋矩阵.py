# 可以将矩阵看成若干层，首先填入矩阵最外层的元素，其次填入矩阵次外层的元素，直到填入矩阵最内层的元素。
#
# 分层思想，引入4个指针left,right,bottom,top。每填满一层调整指针进入下一层填入。
# [[1, 1, 1, 1, 1, 1],
#  [1, 2, 2, 2, 2, 1],
#  [1, 2, 3, 3, 2, 1],
#  [1, 2, 3, 3, 2, 1],
#  [1, 2, 2, 2, 2, 1],
#  [1, 1, 1, 1, 1, 1]]

# n -> Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# 来源：力扣（LeetCode）


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nSqu = n ** 2
        print(nSqu)
        matrix = [[0 for i in range(n)] for j in range(n)]
        start = 1
        top=0
        left = 0
        right = n-1
        bottom = n-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                matrix[top][i]=start
                start+=1
            for i in range(top+1,bottom+1):
                matrix[i][right]=start
                start+=1
            for i in range(right-1,left,-1):
                matrix[bottom][i]=start
                start+=1
            for i in range(bottom,top,-1):
                matrix[i][left]=start
                start+=1
            left+=1
            top+=1
            right-=1
            bottom-=1
        return matrix
