#蔡氏公式的變數
year = int(input("Enter the year: "))
c = str(year)[0:2]
y = str(year)[2:4]
month = int(input("Enter the month: "))

#1月等於13月，2月等於14月，其他不變
if month == 1 or month == 2:
    month = month + 12

print("Sun Mon Tue Wed Thu Fri Sat")

#大月31天
if (
    month == 13
    or month == 3
    or month == 5
    or month == 7
    or month == 8
    or month == 10
    or month == 12
):
    for d in range(1, 32):
        w = int(y) + (int(y) // 4) + (int(c) // 4) - 2 * int(c) + (26 * (month + 1) // 10) + d - 1
        #day=特定日的星期:星期日=0，星期一=1，......，星期六=6
        day = w % 7
        if d == 1:
            print("    " * (day - 0), end="")
        #星期六以後跳行
        #d轉成字串、格式化:數字至少兩位數
        if day == 6:
            d = str(d).zfill(2)
            print(f"{d}")
        else:
            d = str(d).zfill(2)
            print(f"{d}", end="  ")
elif month == 14:
    # check if is leap year
    #2月在閏年29天
    if year % 4 == 0 and year % 100 != 0:
        for i in range(1, 30):
            w = int(y) + (int(y) // 4) + (int(c) // 4) - 2 * int(c) + (26 * (month + 1) // 10) + d - 1
            day = w % 7
            if d == 1:
                print("    " * (day - 0), end="")
            if day == 6:
                d = str(d).zfill(2)
                print(f"{d}")
            else:
                d = str(d).zfill(2)
            print(f"{d}", end="  ")
    elif year % 4 == 0 and year % 400 == 0:
        for i in rangr(1, 30):
            w = int(y) + (int(y) // 4) + (int(c) // 4) - 2 * int(c) + (26 * (month + 1) // 10) + d - 1
            day = w % 7
            if d == 1:
                print("    " * (day - 0), end="")
            if day == 6:
                d = str(d).zfill(2)
                print(f"{d}")
            else:
                d = str(d).zfill(2)
                print(f"{d}", end="  ")
    #2月在非閏年28天
    else:
        for i in range(1, 29):
            w = int(y) + (int(y) // 4) + (int(c) // 4) - 2 * int(c) + (26 * (month + 1) // 10) + d - 1
            day = w % 7
            if d == 1:
                print("    " * (day - 0), end="")
            if day == 6:
                d = str(d).zfill(2)
                print(f"{d}")
            else:
                d = str(d).zfill(2)
                print(f"{d}", end="  ")
else:
    # same pattern as above but for the rest of the months
    for d in range(1, 31):
        w = int(y) + (int(y) // 4) + (int(c) // 4) - 2 * int(c) + (26 * (month + 1) // 10) + d - 1
        day = w % 7
        if d == 1:
            print("    " * (day - 0), end="")
        if day == 6:
            d = str(d).zfill(2)
            print(f"{d}")
        else:
            d = str(d).zfill(2)
            print(f"{d}", end="  ")

#會計系 H14126173 賈閔之
