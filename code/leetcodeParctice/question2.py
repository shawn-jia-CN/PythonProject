"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        addition = 0
        ans = None
        tmp = None
        while (l1 or l2 or addition):
            if (l1 and l2) :
                sum = (l1.val + l2 .val+ addition) % 10
                addition = (l1.val + l2 .val+ addition) // 10
            elif (l1) :
                sum = (l1.val + addition) % 10
                addition = (l1.val + addition) // 10    
            elif(l2):
                sum = (l2.val + addition) % 10
                addition = (l2.val + addition) // 10    
            else:
                sum = addition
                addition = 0      
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if ans == None:
                tmp = ListNode(val=sum)
                ans = tmp
            else:
                tmp.next = ListNode(val=sum)
                tmp = tmp.next
        return ans


