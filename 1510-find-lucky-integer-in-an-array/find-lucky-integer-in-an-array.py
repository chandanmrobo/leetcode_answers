from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
            return max((num for num, count in Counter(arr).items() if num == count), default=-1)


                            