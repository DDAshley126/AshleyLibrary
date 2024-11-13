class Solution:
    def romanToInt(self, s: str) -> int:
        s_sum = 0
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i, num in enumerate(s):
            if i < len(s)-1 and values[s[i]] < values[s[i+1]]:
                s_sum = -values[s[i]] + s_sum
            else:
                s_sum = values[s[i]] + s_sum
        return s_sum