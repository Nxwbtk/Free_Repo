# ********************************************************************************* #
#                                                                                   #
#                                                      :::     ::: :::     :::      #
#    Dony.py                                          :+:    :+:  :+:     +:+       #
#                                                    +:+   +:+   +:+     +:+        #
#    By: nxwbtk <bunthakan.s@ku.th>                 +#+  +:+    +#+     +#+         #
#                                                  +#+ #+#     +#+     +#+          #
#    Created: 2022/07/15 23:33:22 by nxwbtk       #+#   #+#   +#+     +#+           #
#    Updated: 2022/07/15 23:34:16 by nxwbtk      ###     ###   ########.th          #
#                                                                                   #
# ********************************************************************************* #

from cmath import sqrt

#1
try:
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))
    area = width * length
    print(f"{area = }")
except:
    print("Please enter number only!")

#2
try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = sqrt((x ** 2) + (y ** 2))
    print(f"{z = }")
except:
    print("Please enter number only!")

#3
try:
    r = float(input("Enter your radian: "))
    area = ((22 / 7) * (r ** 2))
    circumference = (2 * (22 / 7) * r)
    print(f"{area = } , {circumference = }")
except:
    print("Enter number only!")

#4
try:
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    bmi = weight / (height ** 2)
    print(f"{bmi = }")
except:
    print("Enter number only!")

#5
try:
    money = float(input("Enter your money: "))
    price = float(input("Enter oil price per liter: "))
    liter = money / price
    int(liter)
    change = money % price
    print(f"{liter = } , {change = }")
except:
    print("Enter number only!")

#6
name = input("Enter your name: ")
print(f"Thank you for buying items, {name}")
