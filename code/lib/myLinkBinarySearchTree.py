from collections import deque

class TreeNode:
    def __init__(self, data : int):
        self.val : int = data
        self.left : TreeNode | None = None 
        self.right : TreeNode | None = None

def level_order(root : TreeNode) -> list[int]:
    res : list[int] = []
    queue : deque[TreeNode] = deque()
    queue.append(root)
    while len(queue)> 0:
        tmp = queue.popleft()
        res.append(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)
    return res

def treeInit() -> TreeNode:
    root = TreeNode(8)
    n1 = TreeNode(4)
    n2 = TreeNode(12)
    root.left = n1
    root.right = n2
    n3 = TreeNode(2)
    n4 = TreeNode(6)
    n5 = TreeNode(10)
    n6 = TreeNode(14)
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right =n6

    n7 = TreeNode(1)
    n8 = TreeNode(3)
    n9 = TreeNode(5)
    n10 = TreeNode(7)
    n11 = TreeNode(9)
    n12 = TreeNode(11)
    n13 = TreeNode(13)
    n14 = TreeNode(15)
    n3.left = n7
    n3.right = n8
    n4.left = n9
    n4.right = n10
    n5.left = n11
    n5.right = n12
    n6.left = n13
    n6.right = n14
    return root

def search(root : TreeNode, val : int) ->  TreeNode:
    if root == None or root.val == val:
        return root
    current = root
    while current is not None:
        if val > current.val:
            current = current.right
        elif val < current.val:
            current = current.left
        else:
            break
    return current

def insert(root : TreeNode, val : int) -> None:
    if root == None:
        root = TreeNode(val)
        return
    
    pre, cur = None, root
    while cur is not None:
        if cur.val == val:
            return 
        pre = cur
        if val > cur.val:
            cur = cur.right
        else:
            cur = cur.left
    
    tmp = TreeNode(val)
    if  pre.val > val :
        pre.left = tmp
    else:
        pre.right = tmp
    return 


def remove(root : TreeNode, val : int) -> None:
    if root ==  None:
        return
    
    tmp, pre = root, None
    while tmp is not None:
        if tmp.val == val:
            break
        pre = tmp
        if tmp.val > val:
            tmp = tmp.left
        else:
            tmp = tmp.right

    if tmp == None:
        return 
    
    if tmp.left == None or tmp.right == None:
        child = tmp.left or tmp.right
        if tmp == root:
            root = child
        else:
            if tmp == pre.left:
                pre.left = child
            else:
                pre.right = child
    else:
        p = tmp.right
        while p.left is not None:
            p = p.left
        remove(root, p.val)
        tmp.val = p.val






def run() -> None :
    root = treeInit()
    print(level_order(root))
    if search(root, -1):
        print("found")
    else:
        print("Not found")

    insert(root, 21)
    print(level_order(root))
    insert(root, -1)
    print(level_order(root))
    remove(root, 21)
    print(level_order(root))
    remove(root, 8)
    print(level_order(root))
    


if __name__ == "__main__":
    run()


