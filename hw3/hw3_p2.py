# expression = "X^5+3*X+2"
# expression = "-X^3-12*X^2+100"
# expression = "X^X+X*X+X"
# expression = "X^4+23*X^3+17*X^2+9453" # 有問題第73行報錯: invalid literal for int() with base 10: '' # multiplier = ''
# expression = "X^3 + 3^9"
expression = input("Input polynomial: ")
x_value = int(input("Input the value of X: "))

# 找指數: coefficient^exponent
while "^" in expression:
  index = expression.find("^")

  coefficient = ""
  for i in range(index - 1, -1, -1):
    if (expression[i] == "+" or expression[i] == "-" or expression[i] == "*"
        or expression[i] == " "):
      break
    coefficient = expression[i] + coefficient
    print(f"coefficient: {coefficient}")

  exponent = ""
  for i in range(index + 1, len(expression), 1):
    if (expression[i] == "+" or expression[i] == "-" or expression[i] == "*"
        or expression[i] == " "):
      break
    exponent = exponent + expression[i]
    print(f"exponent: {exponent}")

  term_string = coefficient + "^" + exponent
  print(f"term_string: {term_string}")
  if coefficient == "X" and exponent == "X":
    term_value = int(x_value)**int(x_value)
  elif coefficient == "X":
    term_value = int(x_value)**int(exponent)
  elif exponent == "X":
    term_value = int(coefficient)**int(x_value)
  else:
    term_value = int(coefficient)**int(exponent)
  print(f"term_value: {term_value}")

  #replace the term as value
  expression = expression.replace(term_string, str(term_value))
  print(f"expression: {expression}")

# 找乘數: multiplicand * multiplier
while "*" in expression:
  index = expression.find("*")

  multiplicand = ""
  for i in range(index - 1, -1, -1):
    if (expression[i] == "+" or expression[i] == "-" or expression[i] == " "):
      break
    multiplicand = expression[i] + multiplicand
  print(f"multiplicand: {multiplicand}")

  multiplier = ""
  for i in range(index + 1, len(expression), 1):
    if (expression[i] == "+" or expression[i] == "-" or expression[i] == " "):
      break
    multiplier = multiplier + expression[i]
  print(f"multiplier: {multiplier}")

  term_string = multiplicand + "*" + multiplier
  if multiplicand == "X" and multiplier == "X":
    term_value = int(x_value) * int(x_value)
  elif multiplicand == "X":
    term_value = int(x_value) * int(multiplier)
  elif multiplier == "X":
    term_value = int(multiplicand) * int(x_value)
  else:
    term_value = int(multiplicand) * int(multiplier)
  print(f"term_value: {term_value}")
  # replace the term as value
  expression = expression.replace(term_string, str(term_value))

# final = "32+6+2"
# final = "32-6+2"
# final = "--32-6+2"
final = expression
result = 0
if "X" in final:
  final = final.replace("X", str(x_value))
if "-" not in final:
  pass
else:
  if "-" in final:
    final = final.replace("-", "+-")
  elif "--" in final:
    final = final.replace("--", "+")
    final = final.replace("-", "+-")
temp = final.split("+")
print(f"temp: {temp}")

for value in temp:
  print(f"value: {value}")
  if value == "":
    value = 0
  result = result + int(value)
print(f"Evaluated Result: {result}")

#會計系 H14126173 賈閔之
