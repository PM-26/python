# WAP to print the sum of all the primes between a range.
def isPrime(number):
    flag=0
    if ((number==1) or (number<=0)):
        return False
    for i in range(1,number+1):
        if (number%i==0):
            flag=flag+1
    if (flag==2):
        return True
sum=0
for i in range(1,100):
    if isPrime(i):
        sum=sum+i
print(sum)