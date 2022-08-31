# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


s = "(]"
s = "()()("
s = "()()[()])"
s= "[[]]()"
s= "({{{{}}}))"
s= "([)]"

#Every character should cancel out at the end, so if anything is left, remove it.
def matching(s):
    legend = {"]":"[", ")": "(", "}": "{" }
    storage = []    

    for char in s:
        #If not a closing, add to the storage
        if char not in legend:
            storage.append(char)
            continue

        #If a closing and no matching opening, is false
        if char in legend and legend[char] not in storage:
            return False
        
        #If a closing and opening does not match, is false
        if char in legend and storage[-1] != legend[char]:
            return False

        #Otherwise, it matches and should be removed from the list
        storage.pop()

        #print(storage)

    if storage == []:
        return True
    return False

#print(matching(s))