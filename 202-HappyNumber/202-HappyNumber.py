class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            if n in seen:
                break
            
            seen.add(n)
            
            n_copy = n
            new_n = 0
            
            while n_copy != 0:
                new_n += (n_copy % 10) ** 2
                
                n_copy = n_copy // 10
            
            if new_n == 1:
                return True
            
            n = new_n
            
        return False