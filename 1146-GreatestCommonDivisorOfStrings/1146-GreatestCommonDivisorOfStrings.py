# Last updated: 6/22/2025, 2:50:49 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        if str1 + str2 != str2 + str1:
            return ""
        
        gcdlen = gcd(len(str1), len(str2))
        return str1[:gcdlen]

'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        if n < m:
            str1, str2 = str2, str1
            n, m = m, n
        
        max_pre = ""
        for i in range(1, m + 1):
            if n % i or m % i:
                continue
            
            pre = str2[:i]
            if pre * (n // i) == str1 and pre * (m // i) == str2:
                max_pre = pre
        
        return max_pre
'''