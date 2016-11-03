import math

for a in range (1,1000):
    for b in range (1,1000):
        if a + b + math.sqrt((a*a) + (b*b)) == 1000:
            c = math.sqrt((a*a) + (b*b))
            m = a
            n = b
            break

print(m)
print(n)
print(c)
print(m*n*c)
        
