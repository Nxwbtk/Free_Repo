# ********************************************************************************* #
#                                                                                   #
#                                                      :::     ::: :::     :::      #
#    work.py                                          :+:    :+:  :+:     +:+       #
#                                                    +:+   +:+   +:+     +:+        #
#    By: nxwbtk <bunthakan.s@ku.th>                 +#+  +:+    +#+     +#+         #
#                                                  +#+ #+#     +#+     +#+          #
#    Created: 2022/07/24 20:05:37 by nxwbtk       #+#   #+#   +#+     +#+           #
#    Updated: 2022/07/24 20:05:41 by nxwbtk      ###     ###   ########.th          #
#                                                                                   #
# ********************************************************************************* #

try:
    checkin = int(input("Enter your check in time : "))
    checkout = int(input("Enter your check out time : "))
    time = checkout - checkin
    if (checkin > 8 and checkout < 17):
        money = 1000 - ((1000 * 20) / 100)
        late_morning = checkin - 8
        late_evening = 17 - checkout
        print(f"work {time = } hour late {late_morning} hour, Check out early {late_evening} hour and you earn {money = } baht")
    elif (checkin > 8):
        money = 1000 - ((1000 * 10) / 100)
        late_morning = checkin - 8
        print(f"work {time = } hour late {late_morning} hour and you earn {money = } baht")
    elif (checkout < 17):
        money = 1000 - ((1000 * 10) / 100)
        late_evening = 17 - checkout
        print(f"work {time = } hour Check out early {late_evening} hour and you earn {money = } baht")
    elif (checkin <= 8 and checkout >= 17):
        money = 1000
        print(f"work {time = } and you earn {money} baht")
except:
    print("Please enter integer only")

