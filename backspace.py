"""
You are given an array containing two strings. The strings contain keypresses of printable characters and "-B" separated by commas. "-B" is considered a backspace. Return true if the strings form the same word, return False if not.
Example input:
input = ["c,a,r,d","c,a,r,-B,r,d"]
output: True
Explained: As we type out the first string, we just type 'c','a','r','d' to make the word 'card'. The second keypresses are 'c', 'a', 'r', backspace, 'r', 'd'. Both of these sets of keypresses will give us the word "card".
"""

from dataclasses import replace




a = "c,a,r,d"
b = a.split(",")
print(b)


# def finder(w1):
#     #Remove the commas in odd positions
#     corrected1 = ""
#     for i in range(0,len(w1),2):
#         corrected1+=(w1[i])
#     print(corrected1)

#     #Check for -B
#     removed1 = ""
#     for i in range(0,len(corrected1)-1):
#         #Remove previous letter if -B
#         if corrected1[i] == "-" and corrected1[i+1] == "B":
#             removed1 = removed1[::-1]
#         #Keep moving if the B in -B
#         elif corrected1[i] == "B" and corrected1[i-1] == "-":
#             continue
#         else:
#             removed1+= corrected1[i]
#     #Does not go through last letter, check that now
#     if corrected1[-1] != "B":
#         removed1 += corrected1[-1]
#     elif corrected1[-1] == "B" and corrected1[-2] != "-":
#         removed1 += "B"
#     print(corrected1[-1])
#     print(removed1)









# finder("c,a,r,-B,x")


    # #Cycling through the words for -B
    
    # for i in range(len(w1)-1):
    #     if w1[i] == "-" 
