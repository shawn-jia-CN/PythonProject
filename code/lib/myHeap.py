class head:
    def __init__(self, data : list[int]):
        self.data = data
        for index in range(self.parent(len(self.data) - 1), -1, -1):
            self.shif_down(index)
    
    def is_empty(self) -> bool :
        return len(self.data) == 0
    
    def left(self, index : int) -> int :
        return 2 * index + 1
    
    def right(self, index : int) -> int:
        return 2 * index + 2
    
    def parent(self, index):
        return (index - 1)  // 2
    
    def val(self, index: int) -> int:
        if index < 0 or index >= len(self.data):
            return None
        return self.data[index]
 
    def peek(self) -> int :
        if self.is_empty():
            return None
        return self.data[0]

    def insert(self, val : int) :
        self.data.append(val)
        print(self.data)
        self.shif_up(len(self.data) - 1)

    def pop(self) -> int:
        if self.is_empty():
            return None
        val = self.peek()
        self.swap(len(self.data) - 1, 0)
        self.data.pop()
        self.shif_down(0)
        return val

    def shif_up(self, index):
        while index > 0 and self.data[self.parent(index)] < self.data[index] :
            self.swap(index, self.parent(index))
            index = self.parent(index)
        return

    def shif_down(self, index):
        while True:
            l, r, ma = self.left(index), self.right(index), index
            if l < len(self.data) and self.data[l] > self.data[ma]:
                ma = l
            if r < len(self.data) and self.data[r] > self.data[ma]:
                ma = r
            if ma == index:
                break
            self.swap(ma, index)
            index = ma           

    def swap(self, src : int, dst : int):
        if src < 0 or src >= len(self.data):
            return 
        if dst < 0 or dst >= len(self.data):
            return    
        tmp = self.data[src]
        self.data[src] = self.data[dst]
        self.data[dst] = tmp
        return
     
    def level_order(self) -> list[int]:
        return self.data

def run():
    h = head([1, 2, 3, 4, 5])
    h.pop()
    h.insert(10)
    print(h.level_order())
    pass

if __name__ == "__main__":
    run()