# Read input n
n = int(input("Enter n to retrieve the nth number from the Fibonacci Sequence: "))

# Calculate the nth Fibonacci number to use as the key for Caesar Cipher
if n <= 1:
    fibonacci = n
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    fibonacci = b

# Read two different strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find the lengths of the longest palindromic substrings for both strings
max_length1 = 0
longest_substring1 = ""
for i in range(len(string1)):
    for j in range(i + 1, len(string1) + 1):
        substr = string1[i:j]
        if substr == substr[::-1] and len(substr) > max_length1:
            max_length1 = len(substr)
            longest_substring1 = substr

max_length2 = 0
longest_substring2 = ""
for i in range(len(string2)):
    for j in range(i + 1, len(string2) + 1):
        substr = string2[i:j]
        if substr == substr[::-1] and len(substr) > max_length2:
            max_length2 = len(substr)
            longest_substring2 = substr

# Read the plaintext to be encrypted
plaintext = input("Enter the plaintext: ")

# Caesar Cipher encryption
caesar_cipher = ""
for char in plaintext:
    if char.isalpha():
        shifted_char = chr((ord(char) - ord('a') + fibonacci) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + fibonacci) % 26 + ord('A'))
        caesar_cipher += shifted_char
    else:
        caesar_cipher += char

# Affine Cipher encryption
affine_key_a = len(longest_substring1)
affine_key_b = len(longest_substring2)

affine_cipher = ""
for char in caesar_cipher:
    if char.isalpha():
        if char.islower():
            affine_cipher += chr(((ord(char) - ord('a')) * affine_key_a + affine_key_b) % 26 + ord('a'))
        else:
            affine_cipher += chr(((ord(char) - ord('A')) * affine_key_a + affine_key_b) % 26 + ord('A'))
    else:
        affine_cipher += char

# Output the encrypted text
print("Encrypted text:", affine_cipher)

#會計系 H14126173 賈閔之