import random

class RandomPrime:
    #generate primes up to limit using Sieve of Eratosthenes
    def prime_sieve(self,limit):
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
    def __init__(self,primeCount):
        self.first_primes_list = self.prime_sieve(primeCount)
    #Random odd number
    #Check against first 100 primes
    #Miller-Rabin
    def getPrime(self,n): 
        while True: 
            p = random.randrange(2**(n-1)+1, 2**n-1,2)
            for div in self.first_primes_list: 
                if p % div == 0 and div**2 <= p:
                    break
                else: 
                    return p

    # psudocode copied from:
    # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    # input is a single odd integer
    def isMillerRabin(self,n):
        #Calcuate s and d so that n-1 = 2^s * d
        d = n-1
        s=0
        # factor out the powers of two and rewrite the number in the form 2^s * d
        while d%2==0:
            d = d // 2
            s+=1
        for i in range(20):
            a = random.randrange(2, n-2)
            x = pow(a,d,n)
            for j in range(s):
                y = pow(x,2,n)
                if y==1 and x!=1 and x!=n-1:
                    return False
                x=y
            if y!=1:
                return False
        return True

    def generatePrime(self,size):
        #size of the number to be generated in bits
        primeFound=False
        while not primeFound:
            p=self.getPrime(size)
            if self.isMillerRabin(p):
                return p
    def primeTest(self,p):
        for div in self.first_primes_list: 
            if p % div == 0 and div**2 <= p:
                return False
        return self.isMillerRabin(p)



# x = RandomPrime(100)
# h = x.generatePrime(1024)
# input()

# import time
# endTimes=[]
# for i in range(100):
#     start_time = time.time()
#     x.generatePrime(1024)
#     endTimes.append(time.time()-start_time)

# from statistics import mean
# print(endTimes)
# print(mean(endTimes))
# #AVG of about 1.53 seconds/prime
