class OrderedStream:

    def __init__(self, n: int):
        self.res=['']*n
        print(self.res)
        self.ptr=0
    

    def insert(self, idKey: int, value: str) -> List[str]:
        self.res[idKey-1]=value
        if idKey-1==self.ptr:
            pre_ptr=self.ptr
            while self.ptr<len(self.res) and self.res[self.ptr]:
                self.ptr+=1
            return self.res[pre_ptr:self.ptr]
    


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)