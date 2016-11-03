x = 0
#f = 0
#p = 3
#i = 2

import math

def is_prime(x):
    if x % 2 == 0:
        return False
    for y in range(3,int(math.sqrt(x)),2):
        if x % y == 0:
            return False
    return True

#while f == 0:
 #   if is_prime(p):
  #      if i < 10001:
   #         i += 1
    #    else:
     #       f = 1
      #      break
    #p += 2

m = 104731

while is_prime(m) is False:
    m = m + 2

    
print(m)
    
