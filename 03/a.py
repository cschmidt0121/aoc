f = open("input.txt", "r")
data = f.read()
lines = data.splitlines()

a = [0, 0]
b = [0, 0]
c = [0, 0]
d = [0, 0]
e = [0, 0]
f = [0, 0]
g = [0, 0]
h = [0, 0]
i = [0, 0]
j = [0, 0]
k = [0, 0]
l = [0, 0]

bits = [a,b,c,d,e,f,g,h,i,j,k,l]

for line in lines:
    for i, c in enumerate(line):
        c_to_int = int(c)
        if c_to_int == 0:
            bits[i][0] = bits[i][0] + 1
        else:
            bits[i][1] = bits[i][1] + 1

gamma = ""
epsilon = ""

for i in range(0, len(bits)):
    if bits[i][0] > bits[i][1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"


print(f"Answer is: {int(gamma, 2) * int(epsilon, 2)}")
