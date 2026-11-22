class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        subar=set(nums)
        ind=[]
        for i in range(len(nums)):
            if nums[i]-1 not in subar:
                ind.append(i)
        i=0
        maxlen=0
        while i<len(ind):
            currlen=1
            k=nums[ind[i]]
            while k+1 in subar:
                currlen+=1
                k+=1
            if currlen>maxlen:
                maxlen=currlen
            i+=1
        return maxlen
        