# 要求使用者輸入一個數字 n
#method 1
n = int(input("Input the range number: "))
print("Perfect numbers: ")

# 迭代從2到n的每個數字，查找完美數
for num in range(2, n + 1):
    # 初始化一個變量來存儲因數的總和
    divisor_sum = 1  # 每個數字至少都有1作為因數
    # 查找因數
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisor_sum += i

    # 檢查是否為完美數
    if divisor_sum == num:
        print(num)

#method 2
'''
# 要求使用者輸入一個數字 n
n = int(input("Input the range number: "))
perfect_num = []
# 迭代從2到n的每個數字，查找完美數
for num in range(2, n + 1):
    # 初始化一個變量來存儲因數的總和
    divisor_sum = 0  # 每個數字至少都有1作為因數

    # 查找因數
    for i in range(1, num + 1):
        if num % i == 0:
          divisor_sum += i

    # 檢查是否為完美數
    if divisor_sum / 2 == num:
        perfect_num.append(num)

print("Perfect numbers: ", perfect_num)
'''

#會計系 H14126173 賈閔之