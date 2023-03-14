
def isPrime(x):
    for i in range(2,int(x**(1/2)+1)):
        if (x%i) == 0:
          return False
    return True

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
x=100000000
p = prime_sieve(x)
c=0
for i in p:
    if not isPrime(i*2+1):
        c+=1
print(c/x)