class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.live_time=timeToLive
        self.token={}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId]=self.live_time+currentTime

        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token:
            if self.token[tokenId]>currentTime:
                self.token[tokenId]=currentTime+self.live_time
            else:
                del self.token[tokenId]
        
    def countUnexpiredTokens(self, currentTime: int) -> int:

        count=0
        old=[]
        for key, val in self.token.items():
            if val > currentTime: count+=1
            else:
                old.append(key)
        for key in old:
            del self.token[key]
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)