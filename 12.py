l = [] #list of factors
n = 0 #triangle number
i = 1
x = 0

def factor(x):
    f = [] #list of factors of x
    for y in range (1, x):
        if x%y == 0:
            f.extend([y])
    return f

while len(l) <= 500:
    n = n + i
    l = factor(n)
    i += 1
    
print (l)
