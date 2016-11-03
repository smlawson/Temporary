x = 0
s = 0

import math

def is_prime(x):
    if x % 2 == 0 and x != 2:
        return False
    for y in range(3,int(math.sqrt(x)),2):
        if x % y == 0:
            return False
    return True

for i in range (11,2000000,2):
    if is_prime(i):
        s = s + i

print(s + 17)


