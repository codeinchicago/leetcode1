'''
Done at the ChiPy Algo Night meetup for March 2023.
I originally put lines 37 and 38 together but that failed the edge case of # being the first character in the string. Separating them fixed the problem.

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

def checkword(s1,s2):
    if backspace(s1) == backspace(s2):
        return True
    else:
        return False

def backspace(s):
    word = []
    for letter in s:
        if letter == '#':
            if len(word) !=0:
                word.pop()
        else:
            word.append(letter)
    return word

