"""
23. 合并 K 个升序链表
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""

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

def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
    node = ListNode(0)
    tmp = node
    while l1 and l2:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    if l1 :
        tmp.next = l1
    if l2 :
        tmp.next = l2
    return node.next
            

def mergeKLists(lists: list[ListNode]) -> ListNode:
    if len(lists) <= 0:
        return None
    elif len(lists) == 2:
        return merge2Lists(lists[0], lists[1])
    else:
        return merge2Lists(lists[0], mergeKLists(lists[1:]))


def run():
    tmp = []
    lists = [[1,4,5],[1,3,4],[2,6]]
    for l in lists:
        tmp.append(initWithList(l))
    print(linkToArray(mergeKLists(tmp)))


if __name__ == "__main__":
    run()