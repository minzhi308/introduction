s = input("Enter a string: ")

# Initialize variables to store longest palindromic substring and its length
longest_palindrome = ""
max_length = 0

# Iterate through all possible substrings and check if they are palindromes
for i in range(len(s)): # Iterate i from 0 to len(s) - 1
    for j in range(i + 1, len(s) + 1): # Iterate j from i + 1 to len(s)
        substr = s[i:j]
        # Check if substring is palindrome
        if substr == substr[::-1] and len(substr) > max_length:
            longest_palindrome = substr
            max_length = len(substr)
        #If longest substring = 1, no palindrome
        if max_length == 1:
            longest_palindrome = ""
            max_length = 0

print("Longest palindromic substring:", longest_palindrome)
print("Length is: ",len(longest_palindrome))

"""
這個ouput怎麼debug?(見line16)
Enter a string: gold
Longest palindromic substring: g
Length is:  1
(不符回文定義，回文字串應該是空的，length應=0)
"""

#會計系 H14126173 賈閔之