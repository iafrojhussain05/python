age = int(input("Enter Your age : "))

# first if statement

if age % 2 == 0:
    print(age ,"is Even")
else:
    print(age , "is Odd")    
#end of first if statement


# if elif else leader
# second statement
if age >= 18:
    print("you are adult!")

elif age >= 13 and age <= 17:
    print("You are Teenager")

elif age < 0:
    print("You are entering invalid nagetive age ")

elif age == 0:
    print("You are entering 0 which is not a valid age ")    
else:
    print("you are child!")
# end second statement 

print("End of Program! ")    
#end program