# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# s = "pwwkew"
s = "dvdf"

def longestString(s):
    fail = 0
    length = 0
    inString = set()
    for letter in s:
        if letter in inString:
            inString = set()
        if letter not in inString:
            inString.add(letter)
            # print(inString)
            if length < len(inString):
                length = len(inString)
    return length

print(longestString(s))