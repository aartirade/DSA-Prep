class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = roman[s[-1]]
        for i in range(1, len(s)):

            if roman[s[i-1]] < roman[s[i]]:
                total -= roman[s[i-1]]
            else:
                total += roman[s[i-1]]
        return total
        