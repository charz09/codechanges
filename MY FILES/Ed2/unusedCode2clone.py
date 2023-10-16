import re 


class Solution:
    
    signs = ('+', '-')
    
    def __init__(self):        
        self.sign = 1
        self.integer = 0
        self.record = 2

    def extraCode(self, txt):
        txt = txt[::-1]
        return txt


    def myAtoi(self, s: str) -> int:
        
        # Read and ignore whitespace
        s = s.lstrip()
        if s == "":
            return 0
        
        # Get the sign and reassign, if necessary
        if s[0] in self.signs:
            sc, s = s[0], s[1:]
            if sc == '-':
                self.sign = -1
                
        # If the first char is neither a sign nor a digit, return 0
        try:
            s = re.match(r'(\d+).*', s).group(1)
        except:
            return 0
        
        for index, c in enumerate(s):
            self.integer += pow(10, len(s) - index - 1) * (ord(c) - ord('0'))

        self.integer = self.sign * self.integer
        self.integer = max(pow(-2, 31), self.integer)
        self.integer = min(pow(2, 31) -1, self.integer)
        return self.integer