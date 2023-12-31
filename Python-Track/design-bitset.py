class Bitset:

    def __init__(self, size: int):

        self.oneSet=set()
        self.size=size
        self.flipped=False
        

    def fix(self, idx: int) -> None:
        if self.flipped:
            if idx in self.oneSet:
                self.oneSet.remove(idx)
        else:
            self.oneSet.add(idx)
        

    def unfix(self, idx: int) -> None:
        if self.flipped:
            self.oneSet.add(idx)
        else:
            if idx in self.oneSet:
                self.oneSet.remove(idx)

        
    def flip(self) -> None:
        if self.flipped: self.flipped=False
        else: self.flipped=True

    def all(self) -> bool:
        if self.flipped:
            return len(self.oneSet)==0
        else:
            return len(self.oneSet)==self.size

    def one(self) -> bool:
        if self.flipped:
            return len(self.oneSet)<self.size
        else:
            return len(self.oneSet)>0

    def count(self) -> int:
        if self.flipped:
            return self.size-len(self.oneSet)
        else:
            return len(self.oneSet)

    def toString(self) -> str:
        
        res=[]
        if self.flipped:
            for i in range(self.size):
                if i not in self.oneSet:
                    res.append(1)
                else:
                    res.append(0)
        else:
            for i in range(self.size):
                if i in self.oneSet:
                    res.append(1)
                else:
                    res.append(0)
        return ''.join(str(x) for x in res)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()