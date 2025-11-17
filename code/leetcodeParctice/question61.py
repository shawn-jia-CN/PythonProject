"""
61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def init(l: list[int]) -> ListNode:
    head = None
    tmp = head
    for i in l:
        if head ==  None:
            head  = ListNode(i)
            tmp = head
        else:
            tmp.next = ListNode(i)
            tmp = tmp.next
    return head

def printList(head: ListNode):
    tmp = head
    l = []
    while tmp:
        l.append(tmp.val)
        tmp = tmp.next
    print(l)
    return 
        
def rotateRight(head: ListNode, k: int) -> ListNode:
    if head == None:
        return None
    oldHead:ListNode = head
    oldTail:ListNode = head
    newHead:ListNode = head.next
    newTail:ListNode = head
    tmp = head
    count = 0
    key = 0
    while tmp:
        oldTail = tmp
        tmp = tmp.next
        count = count + 1

    if count == 1:
        return head
    else:
        if k % count == 0:
            return head
        else:
            key = count - k % count - 1
            while key > 0:
                newTail = newTail.next
                newHead = newTail.next
                key = key - 1
            newTail.next = None
            oldTail.next = head
    return newHead


def run():
    head = init([1,2,3])
    printList(head)
    newHead = rotateRight(head, 4)
    printList(newHead)

if __name__ == "__main__":
    run()