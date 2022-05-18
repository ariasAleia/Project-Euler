sum = 0

a = 1
b = 2
"""
for i in range(89+1):
    print(b)
    if(b%2 == 0):
        sum += b

    b = b+a
    a = b-a
"""
while b <= 4000000:
    print(b)
    if(b%2 == 0):
        sum += b

    b = b+a
    a = b-a

print(sum)
