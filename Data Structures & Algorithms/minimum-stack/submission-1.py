class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.min_int = val

        if self.min_int > val:
            self.min_int =  val
        
        self.arr.append([val,self.min_int])

    def pop(self) -> None:
        self.arr.pop()
        if len(self.arr) > 0:

            self.min_int = self.arr[-1][1]
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
