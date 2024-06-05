F = float(input("Input the force: "))
m1 = float(input("Input the mass of m1: "))
r = float(input("Input the distance: "))

G = 6.67 * (10 ** (-11)) #重力常數
m2 = F / G * (r ** 2) / m1 #萬有引力方程式
c = 299792458 #m/s
E= m2 * (c ** 2) #質能守恆方程式

print("The mass of m2 = " , m2)
print("The energy of m2 = " , E)
