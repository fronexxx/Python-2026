class Solution:
    @staticmethod
    def roman_to_int(s: str) -> int:
        roman_to_int = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        result = 0

        for i, num in enumerate(s):
            if i + 1 < len(s) and roman_to_int[num] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[num]
            else:
                result += roman_to_int[num]

        return result


print(Solution.roman_to_int('XV'))

s = 'XV'

print(len(s))


