class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occmap={}
        key = list(set(arr))
        for i in key:
            occmap[i]=arr.count(i)
        return len(set(occmap.values())) == len(occmap.values())
            