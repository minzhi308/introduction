# 要求使用者輸入 Fibonacci 數列項數
n = int(input("Input an integer number:"))

# 設定前兩項 Fibonacci 數字
fibonacci_0 = 0
fibonacci_1 = 1

# 如果 n 為 0 或 1
if n == 0:
  print("The", str(n) + "-th Fibonacci number is:", fibonacci_0)
elif n == 1:
  print("The", str(n) + "-th Fibonacci number is:", fibonacci_1)
else:
  count = 2
  while count <= n:
    # 計算下一項 Fibonacci 數
    next_fibonacci = fibonacci_0 + fibonacci_1
    # 更新前兩項數值:上一輪的第二項是這輪第一項，上一輪的第三項是這輪第二項
    fibonacci_0 = fibonacci_1
    fibonacci_1 = next_fibonacci
    # 更新count，不然count永遠等於2
    count += 1
    
  
  print("The", str(n) + "-th Fibonacci number is:", next_fibonacci)

#會計系 H14126173 賈閔之