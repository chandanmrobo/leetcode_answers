class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        re=0
        while x>re:
            re=re*10+x%10
            x //= 10
        return re==x or x==re//10