#!/usr/bin/python3

#1-100 loop
#3の倍数のときは"FIZZ", 5の倍数のときは"BUZZ"
#15の倍数のときは、”FizzBuzz"
#それ以外は数字（1-100）
i=0
def printNum():
    print(f"{i}")
while True:
    i = i + 1
    if i%15 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        printNum()
    
    if i == 100:
        break
