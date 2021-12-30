# https://leetcode-cn.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num1_list = []
        num1 = 0
        l_first = l1
        while l_first is not None:
            num1_list.append(l_first.val)
            l_first = l_first.next
        pos = 0
        for num in num1_list:
            num1+=num * (10 ** pos)
            pos+=1

        num2_list = []
        num2 = 0
        l_second = l2

        while l_second is not None:
            num2_list.append(l_second.val)
            l_second = l_second.next
        pos = 0
        for num in num2_list:
            num2+=num * (10 ** pos)
            pos+=1

        res = num1+num2
        reslist=[]
        while res>=0:
            reslist.append(res%10)
            res/=10
            if res==0:
                break

        # resNode = ListNode(reslist[0],None)
        # resNode1 = ListNode(reslist[1],None)
        # resNode.next = resNode1
        # Node = ListNode(1,None)
        # Node.next = resNode

        # Node = ListNode(1,None)
        # Node1 = ListNode(2,None)
        re = ListNode(0)
        r = re
        # resNode = ListNode(reslist[0],None)
        for i in range(len(reslist)):
            Node = ListNode(reslist[i],None)
            r.next = Node
            r = Node
            print(re)


        return re.next


        # print(reslist)
