h = int(input("Input the height of the 1st ball: "))
m1 = int(input("Input the mass of the 1st ball: "))
m2 = int(input("Input the mass of the 2nd ball: "))

g = 9.8
#算第一顆球在初始高度的位能
U = m1 * g * h

#用力學能守恆定律算兩顆球初速
u1 = (2 * U / m1) ** 0.5
u2 = (2 * U / m2) ** 0.5

#用彈性碰撞定律的公式算兩球碰撞後速度
v1 = ((m1 - m2) * u1 + 2 * m2 * u2) / (m1 + m2)
v2 = ((m2 - m1) * u2 + 2 * m1 * u1) / (m1 + m2)

print("The velocity of the 1st ball after slide: " , u1 ,  "m/s")
print("The velocity of the 2nd ball after collision: " , v2 , "m/s")
