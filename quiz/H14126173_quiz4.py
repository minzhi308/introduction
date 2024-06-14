# Example: Input: 5 6 1 2 3 4
# Output:
# Length:  4
# LICS:  [1, 2, 3, 4]
sequence = input("Enter a sequence of integers seperated by whitespace: ")

# print(sequence)
sequence = sequence.split(" ") # str->list
# print(sequence)
sequence = [int(x) for x in sequence] # char->int
# print(sequence)

temp_LICS =[sequence[0]] # 5
LICS = [] # initial empty

for element in sequence[1:]: #從第 1 位開始尋訪
  if element > temp_LICS[-1]: # temp_LICS[-1]: temp_LICS 中最後一個元素
    temp_LICS.append(element) # 5, 6 # 如果當前元素比 temp_LICS 中最後一個元素大，則將該元素添加到 temp_LICS
  else:
    if len(temp_LICS) > len(LICS): # 如果當前元素不大於 temp_LICS 中的最後一個元素，則比較 temp_LICS 和 LICS 的長度
      LICS = temp_LICS # 5, 6 # 如果 temp_LICS 比 LICS 更長，則將 temp_LICS 賦值給 LICS，表示找到了一個更長的遞增連續子序列
    temp_LICS = [element] # 1 # 重新初始化 temp_LICS 為只包含當前元素的列表

if len(temp_LICS) > len(LICS):
  LICS = temp_LICS

print("Length: ", len(LICS))
print("LICS: ", LICS)

