#芮氏規模
r=float(input("Please enter a Richter scale value: "))
print("Richter scale value: ",r)

#焦耳
j=10**(1.5*r+4.8)
print("Equivalence in Joules: ",j)

#炸藥
t=j/(4.184*(10**9))
print("Equivalence in tons of TNT: ",t)

#營養午餐6
n=j/2930200
print("Equivalence in the number of nutritious lunches: ",n)
