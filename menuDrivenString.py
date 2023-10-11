def concatenate(string1,string2):
    return string1+string2
def multiply(string):
    return string*5
def length(string):
    return len(string)
def areStringsEqual(string1,string2):
    return string1==string2

while True:
    print("\n\tM E N U\t")
    print("1. Concatenate two strings.")
    print("2. Replicate a string 5 times.")
    print("3. Calculate the length of a string.")
    print("4. Check if two strings are equal.")
    print("5. Exit")

    choice=int(input("\nChoose from 1/2/3/4/5 Please->"))
    if (choice==1):
        string1=input("Enter first string:")
        string2=input("Enter second string:")
        print(f"\nConcatenated String-->{concatenate(string1,string2)}")
    elif(choice==2):
        string=input("Enter a string-->")
        print(f"\nReplicated String-->{multiply(string)}")
    elif(choice==3):
        string=input("Enter a string-->")
        print(f"\nLength of string-->{length(string)}")
    elif(choice==4):
        string1=input("Enter the first string--> ")
        string2=input("Enter the second string--> ")
        result=areStringsEqual(string1,string2)
        if(result):
            print("\nThey are equal.")
        else:
            print("\nThey are not equal.")
    elif(choice==5):
        print("\nExiting. . .Bye!Cya!")
        break
    else:
        print(f"\nEnter a valid choice.")
