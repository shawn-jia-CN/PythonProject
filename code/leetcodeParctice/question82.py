"""
82. 删除排序链表中的重复元素 II
给定一个已排序的链表的头 head , 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
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
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy
    while cur.next and cur.next.next:
        val = cur.next.val
        if cur.next.val == cur.next.next.val:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next

def run():
    l = [1,2,3,3,4,4,5]
    head = init(l)
    print(printList(head))
    deleteDuplicates(head)
    print(printList(head))

if __name__ == "__main__":
    run()