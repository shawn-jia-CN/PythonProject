from collections import deque

class TreeNode:
    def __init__(self, val: int):
        self.data : int  = val 
        self.left : TreeNode | None = None 
        self.right : TreeNode | None = None 


def level_order(root : TreeNode) :
    queue : deque[TreeNode] = deque()
    queue.append(root)
    ret = []
    while len(queue):
        tmp = queue.popleft()
        ret.append(tmp.data)
        if tmp.left :
            queue.append(tmp.left)
        if tmp.right :
            queue.append(tmp.right)
    return ret


def pre_order(root : TreeNode):
    if root == None:
        return 
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root : TreeNode):
    if root == None:
        return 
    in_order(root.left)
    print(root.data)
    in_order(root.right)


def post_order(root : TreeNode):
    if root == None:
        return 
    post_order(root.left)
    post_order(root.right)
    print(root.data)

def tree_init() -> TreeNode:
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    return n1


def run():
    root = tree_init()
    print(level_order(root=root))
    print("--------")
    pre_order(root=root)
    print("--------")
    in_order(root=root)
    print("--------")
    post_order(root=root)
    print("--------")


if  __name__ == "__main__":
    run()


