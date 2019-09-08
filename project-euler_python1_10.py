# problem2
a = 1
b = 2
c = 0
sodi = [b]
while a < 4000000 and b < 4000000 and c < 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        sodi.append(c)


# problem 3:
# Python3 code to find largest prime 
# factor of number 
import math 
  
# A function to find largest prime factor 
def maxPrimeFactors (n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = 0
      
    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n /= 2      
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
# problem 4
seznam = []
for i in range(100,1000):
    for j in range(100,1000):
        produkt = str(i * j)
        if produkt[::-1] == produkt:
            seznam.append(int(produkt))

# problem 5
#a*b = gcd(a,b) * lcm(a,b)
import fractions  
def lcm(n): 
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)/math.gcd(int(ans), i)         
    return int(ans) 


# problem 6
vsota_kvadratov = 0
for i in range(101):
    vsota_kvadratov += i ** 2
kvadrat_vsote = sum([i for i in range(101)]) ** 2
#print(kvadrat_vsote - vsota_kvadratov)

#problem 7
def je_prastevilo(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True

def prastevilo(n):
    if n == 1:
        return 2
    count = 1
    num = 1
    while count < n:
        num += 2 
        if je_prastevilo(num):
            count +=1
    return num

# problem 8
stevilo = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
seznam == []
vrsta = str(stevilo)
for i in range(1000):
    produkt = 1
    for num in vrsta[i:i+13]:
        produkt *= int(num)
    seznam.append(produkt)

# problem 9
for a in range(10000):
    for b in range(10000):
        c = (a ** 2 + b ** 2) ** (1 / 2)
        vsota = a + b + c
        if (c).is_integer() and vsota == 1000:
            #print(str(int(a * b * c)))
            break
# problem 10
#ne dela ful hitro
#hi = 2000000
#i = 2
#vsota = 0
#for stevilo in range(i, hi):
#    if je_prastevilo(stevilo):
#        vsota += stevilo
#        i = stevilo
