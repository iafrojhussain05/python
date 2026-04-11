age = int(input("Enter Your age : "))


# if elif else leader

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


print("End of Program! ")    