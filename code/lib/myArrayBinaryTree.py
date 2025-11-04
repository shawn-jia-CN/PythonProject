from collections import deque

class ArrayTree:
    def __init__(self, data : list[int]):
        self.data = data
        self.res = []
        if data:
            self.length = len(self.data)
        else:
            self.length = 0

    def __str__(self):
        ret = ""
        if self.data != None:
            for i in self.data:
                ret += str(i)
        return ret
    
    def getLen(self):
        return self.length
    
    def val(self, index):
        if index < 0 or index > self.length - 1:
            return None
        return self.data[index]

    def left(self, index):
        return 2 * index  + 1
    
    def right(self, index):
        return 2 * index + 2
    
    def parent(self, index):
        return index // 2
    
    def level_order(self):
        self.res = []
        for i in range(self.length):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res
    
    def dfs(self, index, order):
        if self.val(index) == None:
            return 
        
        if order == "pre":
            self.res.append(self.val(index))
        self.dfs(self.left(index), order)
        if order == "in":
            self.res.append(self.val(index))
        self.dfs(self.right(index), order)
        if order == "post":
            self.res.append(self.val(index))

    def pre_order(self):
        self.res = []
        self.dfs(0, "pre")
        return self.res

    def in_order(self):
        self.res = []
        self.dfs(0, "in")
        return self.res

    def post_order(self):
        self.res = []
        self.dfs(0, "post")
        return self.res

def run():

    t = ArrayTree([1,2,3,4,5,6,7])
    print(t.level_order())
    print(t.pre_order())
    print(t.in_order())
    print(t.post_order())
    

if  __name__ == "__main__":
    run()