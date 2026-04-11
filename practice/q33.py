# Write a program to find whether a given number is prime or not.

n = int(input("Enter Number : "))

for i in range(2 , n):
    if(n%i) == 0:
        print(f"{n} is not Prime Number ")
        break
else:   
    print(f"{n} is Prime Number ")