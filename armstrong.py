def armstrong(number):
    digits=[int (d) for d in str(number)]
    sum=([d**3 for d in digits])
    return sum==number
print("Check for armstrong.")
number=int(input("Enter a number-->"))
print(armstrong(number))