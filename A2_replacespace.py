class Solution:
    def replacespace(self, s):
        str = s.split(' ')
        s = '%20'.join(str)
        return s 