"""
25. K 个一组翻转链表
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def initWithList(input : list[int]) -> ListNode:
    if len(input) == 0:
        return None
    head = None
    tmp = None
    for i in input:
        if tmp is None:
            head = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next

    return head
        
    
def linkToArray(input: ListNode) -> list[int]:
    ret = []
    tmp = input
    while tmp is not None:
        ret.append(tmp.val)
        tmp = tmp.next
    return ret
            

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    node = ListNode(0, head)
    queue = deque()
    tmp = head
    start = node
    while start and start.next:
        while len(queue) < k and tmp:
            queue.append(tmp)
            tmp = tmp.next
        index = None
        count = 0
        stopNext = None
        if len(queue) < k:
            break
        while len(queue) > 0:
            index = queue.pop()
            if count == 0:
                stopNext = index.next
            count = count + 1
            start.next = index
            start = start.next
        start.next = stopNext
    return node.next



    

def run():
    print(linkToArray(reverseKGroup(initWithList([1,2,3,4,5]), 3)))


if __name__ == "__main__":
    run()