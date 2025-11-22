"""
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def init(l: list[int]) -> ListNode:
    if len(l) <= 0:
        return None
    head:ListNode = None
    tmp:ListNode = None
    for i in l:
        if not head:
            head = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next
    return head
def printList(head: ListNode) -> list[int]:
    ans: list[int] = []
    tmp = head
    while(tmp):
        ans.append(tmp.val)
        tmp = tmp.next
    return ans


def partition(head: ListNode, x: int) -> ListNode:
    if not head:
        return head
    leftHead: ListNode = ListNode(0)
    leftTail: ListNode = leftHead
    rightHead: ListNode = ListNode(0)
    rightTail: ListNode = rightHead
    tmp = head
    while(tmp):
        if tmp.val < x:
            leftTail.next = ListNode(tmp.val)
            leftTail = leftTail.next
        else:
            rightTail.next =  ListNode(tmp.val)
            rightTail = rightTail.next
        tmp = tmp.next
    leftTail.next = rightHead.next
    return leftHead.next

def run():
    head = init([1,4,3,2,5,2])
    x = 3
    print(printList(partition(head, x)))

if __name__ == "__main__":
    run()