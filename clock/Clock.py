# !/usr/bin/python3
# Clock Program
# Version : 0.0.1
# Date : 6/2/2021

seconds = range(1, 61)
minutes = range(0, 61)
hours = range(0, 25)
days = 0
while days <=30:
    days += 1
    for h in hours:
        print()
        for m in minutes:
            print()
            for s in seconds:
                print(h, ":H ", m, ":M ", s, ":S ")
    if h == 24 and m == 60 and s == 60:
        print("Day:", days)
