class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set_arr = set(arr)
        occurrence = []
        for i in set_arr:
            occurrence.append(arr.count(i))
        return len(occurrence) == len(set(occurrence))