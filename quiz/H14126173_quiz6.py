import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

answer = random.choice(alphabet)
print(f"Answer: {answer}")

# sample the char from the ASCII code 97~122
# "a" -> ASCII  -> 97
# "z" -> ASCII -> 122
# answer_ASCII = random.randint(97, 122)
# print(answer_ASCII)  # 106 -> j
# answer_char = chr(answer_ASCII)
# print(answer_char)

# guess: c, answer: w
counter = 0
histogram = [0, 0, 0, 0, 0, 0, 0]  # a-d, e-h, ..., y-z
# 0-3, 4-7, 8-11
while True:
    counter = counter + 1
    guess = input("Guess the lowercase alphaet: ")

    # guess -> c -> histogram[0] += 1
    # guess -> h -> histogram[1] += 1
    # guess -> q -> histogram[4] += 1

    # print(ord(guess))  # c -> 99
    # print(ord("a"))  # a -> 97

    # 99 - 97 = 2
    # 2 // 4 -> 0

    # h -> 104
    # a -> 97
    # 104 - 97 = 7
    # 7 // 4 -> 1

    # q -> 113
    # a -> 97
    # 113 - 97 = 16
    # 16 // 4 -> 4

    diff = (ord(guess) - ord("a")) // 4  # -> corresponding pair index
    histogram[diff] += 1

    if guess == answer:
        print(f"Congratulations! You guessed the alphabet {answer} in {counter} tries")
        break
    elif guess < answer:
        print("The alphabet you are looking for is alphabetically higher.")
    elif guess > answer:
        print("The alphabet you are looking for is alphabetically lower.")

print("guess Histogram")
print(histogram)
print(f"a - d: {'*' * histogram[0]}")
print(f"e - h: {'*' * histogram[1]}")
print(f"i - l: {'*' * histogram[2]}")
print(f"m - p: {'*' * histogram[3]}")
print(f"q - t: {'*' * histogram[4]}")
print(f"u - x: {'*' * histogram[5]}")
print(f"y - z: {'*' * histogram[6]}")

    
