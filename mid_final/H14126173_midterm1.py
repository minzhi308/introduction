# 第1排 9, 8, 7 九九乘法
i = 9
while i >= 1:
	print()
	j = 9
	while j >= 7:
		print(i,"x",j,"=",i * j,end = "\t\t")
		j -= 1
	i -= 1
print()

# 第2排 6, 5, 4 九九乘法
i = 9
while i >= 1:
	print()
	j = 6
	while j >= 4:
		print(i,"x",j,"=",i * j,end = "\t\t")
		j -= 1
	i -= 1
print()

# 第3排 3, 2, 1 九九乘法
i = 9
while i >= 1:
	print()
	j = 3
	while j >= 1:
		print(i,"x",j,"=",i * j,end = "\t\t")
		j -= 1
	i -= 1

#三層迴圈怎麼做？為何印不出來？
# k = 1
# while k > 3:
# 	print()
# 	i = 9
# 	while i >= 1:
# 		print()
# 		j = (4 - k) * 3
# 		while j >= j + 2:
# 			print(i,"x",j,"=",i * j,end = "\t\t")
# 			j -= 1
# 		i -= 1
# 	k += 1