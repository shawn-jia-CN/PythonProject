"""
24. 两两交换链表中的节点
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""
from collections import deque
N = 2
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
            

def swapPairs(head: ListNode) -> ListNode:
    node = ListNode(0, head)
    queue = deque()
    tmp = head
    start = node
    while start and start.next:
        while len(queue) < N and tmp:
            queue.append(tmp)
            tmp = tmp.next
        index = None
        count = 0
        stopNext = None
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
    print(linkToArray(swapPairs(initWithList([1,2,3,4,5]))))


if __name__ == "__main__":
    run()