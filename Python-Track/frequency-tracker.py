class FrequencyTracker:

    def __init__(self):

        self.add_nums={}
        self.freq_tra={} 

    def add(self, number: int) -> None:

        if number not in self.add_nums:
            self.add_nums[number]=1
            self.freq_tra[1]=self.freq_tra.get(1,0)+1
        else:
            if self.freq_tra[self.add_nums[number]]==1:
                del self.freq_tra[self.add_nums[number]]
            else:
                self.freq_tra[self.add_nums[number]]-=1
            self.add_nums[number]+=1
            self.freq_tra[self.add_nums[number]]=self.freq_tra.get(self.add_nums[number],0)+1
        

    def deleteOne(self, number: int) -> None:
        if number in self.add_nums:
            
            if self.add_nums[number]==1:
                if self.freq_tra[1]==1:
                    del self.freq_tra[1]
                else:
                    self.freq_tra[1]-=1
                del self.add_nums[number]
            else:
                if self.freq_tra[self.add_nums[number]]==1:
                    del self.freq_tra[self.add_nums[number]]
                else:

                    self.freq_tra[self.add_nums[number]]-=1
                self.add_nums[number]-=1    
                self.freq_tra[self.add_nums[number]]=self.freq_tra.get(self.add_nums[number],0)+1
                
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq_tra: return True
        

'''' 
["FrequencyTracker","add","add","add","add","hasFrequency"]
[[],[6],[9],[6],[6],[3]]

["FrequencyTracker","add","add","hasFrequency","hasFrequency","add","add","add"]
[[],[5],[5],[1],[2],[6],[5],[1]]

["FrequencyTracker","add","add","deleteOne","deleteOne","deleteOne","hasFrequency"]
[[],[5],[4],[6],[4],[7],[1]]


'''
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)