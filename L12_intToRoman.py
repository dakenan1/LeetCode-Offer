class Solution:
    #def intToRoman(self, num: int) -> str:
    def intToRoman(self, num):
        m = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]
        mm = num // 1000        
        num = num % 1000 
        dc = num // 100    
        num = num % 100 
        lx = num // 10        
        num = num % 10

        re = [m[0][mm], m[1][dc], m[2][lx], m[3][num]]
        return ''.join(re)

