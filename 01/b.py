#!/usr/bin/env python3
f=open("input.txt", "r")
s=f.read()
readings = s.splitlines()

count = 0 
prev = None
for i in range(0, len(readings) - 2):
    a = int(readings[i])
    b = int(readings[i+1])
    c = int(readings[i+2])

    sum=a+b+c

    if not prev:
        prev = sum
        continue

    if sum > prev:
        count +=1

    prev = sum

print(count)
