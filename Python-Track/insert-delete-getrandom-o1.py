class RandomizedSet:

    def __init__(self):
        self.indice={}
        self.res=[]

    def insert(self, val: int) -> bool:
        if val in self.indice: 
            return False
        self.res.append(val)
        self.indice[val]=len(self.res)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indice:
            return False
        if self.indice!=len(self.res)-1:
            self.res[self.indice[val]]=self.res[-1]
        self.indice[self.res[-1]]=self.indice[val]
        self.res.pop()
        del self.indice[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.res)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()