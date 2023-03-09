import random

#generate primes up to limit using Sieve of Eratosthenes
def prime_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


#Random odd number
#Check against first 100 primes
#Miller-Rabin
def getPrime(n):

    def nBitRandom(n):
        return(random.randrange(2**(n-1)+1, 2**n-1,2))
   
    # Repeat until a number satisfying
    # the test isn't found
    while True: 
   
        # Obtain a random number
        prime_candidate = nBitRandom(n) 

        for divisor in first_primes_list: 
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
                break
            # If no divisor found, return value
            else: 
                return prime_candidate

def isMillerRabinPassed(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
 
    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True
def isPrime(x):
    for i in range(2,int(x**(1/2)+1)):
        if (x%i) == 0:
          return False
    return True

first_primes_list = prime_sieve(100)
for i in range(30):
    #size of the number to be generated in bits
    size=1024
    primeFound=False
    c=0
    while not primeFound:
        c+=1
        p=getPrime(size)
        if isMillerRabinPassed(p):
            primeFound=True
    print(p)
    print(isPrime(p))
    input()
