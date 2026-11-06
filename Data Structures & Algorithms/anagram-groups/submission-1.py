class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li={}

        
        for s in strs:
            key=tuple(sorted(s))

            if key not in li:
                li[key]=[s]
            else:
                li[key].append(s)
        return list(li.values())

            

        