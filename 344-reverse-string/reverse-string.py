class Solution:
    def reverseString(self, s: List[str]) -> None:
        r,l = len(s)-1,0
        while l<r:
            s[r],s[l]=s[l],s[r]
            l+=1
            r-=1
        