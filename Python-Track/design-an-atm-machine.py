class ATM:

    def __init__(self):
        self.banknote={20:0,50:0,100:0,200:0,500:0}
        self.link={0:20,1:50,2:100,3:200,4:500}
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.banknote[self.link[i]]+=banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:

        res=[0]*5

        pre_amount=amount
        if amount>=500 and self.banknote[500]:
            n=amount//500
            if self.banknote[500]>=n:
                self.banknote[500]-=n
                res[4]=n
                amount=amount%500
            else:
                res[4]+=(self.banknote[500])
                amount=500*(n-res[4])+amount%500
                self.banknote[500]=0
            
        if amount>=200 and self.banknote[200]:
            n=amount//200
            if self.banknote[200]>=n:
                self.banknote[200]-=n
                amount=amount%200
                res[3]+=n
            else:
                res[3]+=(self.banknote[200])
                amount=200*(n-res[3])+amount%200
                self.banknote[200]=0
        if amount>=100 and self.banknote[100]:
            n=amount//100
            if self.banknote[100]>=n:
                self.banknote[100]-=n
                amount=amount%100
                res[2]+=n
            else:
                res[2]+=(self.banknote[100])
                amount=100*(n-res[2])+amount%100
                self.banknote[100]=0
            print(amount)
        if amount>=50 and self.banknote[50]:
            n=amount//50
            if self.banknote[50]>=n:
                self.banknote[50]-=n
                amount=amount%50
                res[1]+=n
            else:
                res[1]+=(self.banknote[50])
                amount=50*(n-res[1])+amount%50
                self.banknote[50]=0

        if amount>=20 and self.banknote[20]:
            n=amount//20
            if self.banknote[20]>=n:
                self.banknote[20]-=n
                amount=amount%20
                res[0]+=n
            else:
                res[0]+=(self.banknote[20])
                amount=20*(n-res[0])+amount%20
                self.banknote[20]=0
        if amount>0: 
            for idx, val in enumerate(res):
                self.banknote[self.link[idx]]+=val
            res=[-1]
        return res


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)