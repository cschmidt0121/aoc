#!/usr/bin/env python3
f=open("input.txt", "r")
s=f.read()
readings = s.splitlines()

count = 0 
prev = None
for reading in readings:
    if not prev:
        prev = int(reading)
        continue
    if int(reading) > prev:
        count +=1

    prev = int(reading)


print(count)
