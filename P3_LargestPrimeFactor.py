def isPrime(i):
    prime = True
    j = 2
    
    while(prime and j<i):
        if(i%j == 0):
            prime = False
        j+=1
    return prime

n = 600851475143
for i in range (1, n):
    if(n%i == 0):
        if (isPrime(i)):
            largestPrime = i
            print(i)


