"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
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

def removeNthFromEnd(head : ListNode, n: int) -> ListNode:
    node = ListNode(10**100)
    node.next = head
    count = 0
    tmp = head
    while(tmp is not None):
        tmp = tmp.next
        count = count + 1

    target = count - n
    tmp = node
    for i in range(target):
        tmp = tmp.next
    n = tmp.next
    tmp.next = n.next
    return node.next


def run():
    head = initWithList([1,2,3,4,5])
    print(linkToArray(head))
    print(linkToArray(removeNthFromEnd(head, 5)))


if __name__ == "__main__":
    run()