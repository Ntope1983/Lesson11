# test the program with debugging and breakpoint to find the bug
def max3(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


x = int(input("Give a number: "))
y = int(input("Give a number: "))
z = int(input("Give a number: "))

n = max3(x, y, z)

for i in range(n):
    sq = i * i
    print(sq)
