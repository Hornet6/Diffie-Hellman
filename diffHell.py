import random
def difHellKey(p,g,r):
    print("DIFFHELL")

def genPublicKey(x,p,g):
    k = g**x % p
    return k
def isPrime(x):
    for i in range(2,int(x**(1/2)+1)):
        if (x%i) == 0:
          return False
    return True
def randomPrime(low,high):
    #this needs to be better
    primes = [i for i in range(low,high) if isPrime(i)]
    n = random.choice(primes)
    return n
def genLargePrime(low,high):
    q = randomPrime(int(low/2-1),int(high/2-1))
    return q*2 + 1 
def genPrivateKey(p):
    x = random.radint(1,p)
    return x
print(randomPrime(4,30))
def genSharedKey(pubKeyB,x,p):
    return (pubKeyB**x)%p

def generateGenerator(p):
    
# P is a large random prime
# G is a 

#1.agree on P and G
#2.privKey = genPrivateKey(p)
#3.pubKey = genPublicKey(privKey,p,g)
#4.Share pubKey and get partners public key(pubKeyB)
#5.sharedKey = genSharedKey(pubKeyB,x,p)
#shared key can now be used for encryption
#https://www.math.ucla.edu/~baker/40/handouts/rev_DH/node1.html#:~:text=Example%201.,get%206%20as%20the%20answer.&text=6%20(mod%2010).


#local example:

p = genLargePrime(10**2,10**3)
c=0
ip=0
for i in range(1,10000):
    p = genLargePrime(10**2,10**3)
    # print(p,isPrime(p))
    if isPrime(p):
        ip+=1
    c+=1
print(c,ip)