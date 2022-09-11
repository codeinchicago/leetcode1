"""
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""

s1 = "din"
s1 = "(( @"

def encoder(s1):
    from collections import Counter
    counter = Counter(s1.lower())

    return "".join([")" if counter[ch] > 1 else "(" for ch in s1.lower()])

#print(encoder(s1))