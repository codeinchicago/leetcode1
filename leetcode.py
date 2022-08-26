

from re import S



def isPalindrome(s: str) -> bool:
    lengthToCheck = len(s)//2
    for i in range(lengthToCheck):
        if s[i] != s[-i-1]:
            # print("False")
            # print(s[i])
            # print(s[-i-1])
            return False
    return True


s = 'amanaplanacanalpanama'

print(isPalindrome(s))