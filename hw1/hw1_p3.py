v = float(input("Input the velocity: "))

c = 299792458 #m/s
factor = 1 / ((1- (v ** 2)/(c **2)) ** (1/2)) 
print("Percentage of light speed = " , v / c)

#目的地距離(單位：光年)
timeoflight_Alpha = 4.3
timeoflight_Barnard = 6.0
timeoflight_Betelgeuse = 309
timeoflight_Andromeda = 2000000

＃計算抵達每個目的地所需時間
time_ship1 = time_Alpha / factor
time_ship2 = time_Barnard / factor
time_ship3 = time_Betelgeuse / factor
time_ship4 = time_Andromeda / factor

print("Travel time to Alpha Centauri = " , time_ship1)
print("Travel time to Barnard's Star = ", time_ship2)
print("Travel time to Betelgeuse (in the Milky Way) = ", time_ship3)
print("Travel time to Andromeda Galaxy (closest galaxy) = " , time_ship4)