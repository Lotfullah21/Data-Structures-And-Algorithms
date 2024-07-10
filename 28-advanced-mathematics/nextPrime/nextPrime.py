def prime(n):
    if n<2:
        return False
    c = 0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c<=2:
        return True
    else:
        return False

def nextPrime(n):
    cc = n+1
    while not prime(cc):
        cc+=1
    return cc