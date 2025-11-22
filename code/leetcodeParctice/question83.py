"""
83. 删除排序链表中的重复元素
给定一个已排序的链表的头 head, 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def init(l: list[int]) -> ListNode:
    head = None
    tmp = head
    for i in l:
        if not head:
            head = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next
    return head


def printList(link: ListNode) -> list[int]:
    tmp = link
    ans = []
    while tmp:
        ans.append(tmp.val)
        tmp = tmp.next
    return ans


def deleteDuplicates(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    pre = head
    slow : ListNode = head.next
    fast : ListNode  = head.next
    while fast:
        if pre.val != fast.val:
            slow.val = fast.val
            pre = slow
            slow = slow.next
        fast = fast.next
    pre.next = None
    return head


def run():
    l = [1,2,2,3,3]
    head = init(l)
    print(printList(head))
    deleteDuplicates(head)
    print(printList(head))

if __name__ == "__main__":
    run()