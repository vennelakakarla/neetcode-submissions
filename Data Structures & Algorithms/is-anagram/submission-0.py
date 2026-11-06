class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        for i in range(len(s)):
            dic[s[i]]=dic.get(s[i],0)+1
        for i in range(len(t)):
            dic[t[i]]=dic.get(t[i],0)-1
        return all(v==0 for v in dic.values())
        