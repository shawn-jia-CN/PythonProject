"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
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


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    head = ListNode(0)
    tmp = head
    while list1 and list2:
        if list1.val < list2.val:
            tmp.next = list1
            list1 = list1.next
        else:
            tmp.next = list2
            list2 = list2.next
        tmp = tmp.next

    if list1:
        tmp.next = list1
    if list2:
        tmp.next = list2

    return head.next
    

def run():
    l1 = initWithList([1,2,4])
    l2 = initWithList([1,3,4])
    print(linkToArray(mergeTwoLists(l1, l2)))


if __name__ == "__main__":
    run()