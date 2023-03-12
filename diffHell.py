import random
from randomPrime import RandomPrime
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

def genPrivateKey(p):
    x = random.radint(1,p)
    return x
def genSharedKey(pubKeyB,x,p):
    return (pubKeyB**x)%p

def generate_P_pair(size):
    x = RandomPrime(100)
    while True:
        q=x.generatePrime(size-1)
        q=89005330586580187460447797262694947558585802190639423605895969138137604727030363533383102327238888063774652063166868052487205726446858692415663309318944713324209073763121067320962543994427197072891573532085233436592698772764104874000444566811890847095969397737937311703687348229853815083445001173331555921481
        if x.primeTest(q*2+1):
            return q
# P is a large random prime in the form p=2*q +1 where q is also prime
# G is 2

#1.agree on P and G
#2.privKey = genPrivateKey(p)
#3.pubKey = genPublicKey(privKey,p,g)
#4.Share pubKey and get partners public key(pubKeyB)
#5.sharedKey = genSharedKey(pubKeyB,x,p)
#shared key can now be used for encryption
#https://www.math.ucla.edu/~baker/40/handouts/rev_DH/node1.html#:~:text=Example%201.,get%206%20as%20the%20answer.&text=6%20(mod%2010).


#local example:


p = 89005330586580187460447797262694947558585802190639423605895969138137604727030363533383102327238888063774652063166868052487205726446858692415663309318944713324209073763121067320962543994427197072891573532085233436592698772764104874000444566811890847095969397737937311703687348229853815083445001173331555921481
# p = generate_P_pair(1024)
print(p)
g = 2

# private keys
# A
Xa = random.randrange(p//2,p)
# B
Xb = random.randrange(p//2,p)


#private keys
# A
Ya = pow(g,Xa,p)
# B
Yb = pow(g,Xb,p)

# shared key
# A
Za = pow(Yb,Xa,p)
# B
Zb = pow(Ya,Xb,p)

print(Za==Zb)

