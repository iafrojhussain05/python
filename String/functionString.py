name = "afroj"


# reverse String
print(name[::-1])
# len() function 
print(len(name))

# endswith() 
print(name.endswith("roj"))
print(name.endswith("roz"))

#startswith()
print(name.startswith("Af"))
print(name.startswith("af"))

# capitalize()
print(name.capitalize())

# lower() & upper()
print(name.lower())
print(name.upper())


# strip() extra space remove karta hai 

my_name = "   afroj"
print(my_name) #without using strip() function
print(my_name.strip()) # using strip() fuction


#  replace()
s = "I love Java"
print(s.replace("Java","Python"))

#  split()  String ko list me convert karta hai
fruits = "Apple Banana Mango"
print(fruits.split())



# join()
#  List ko string me convert karta hai
list = ["I","love","Coding"]
print(" ".join(list))


# find() postion (index) batata hai
print(name.find("r"))

# count() use for Kitni baar word aaya
b = "banana"
print(b.count("n"))



# isalpha(), isdigit(), isalnum()
s = "123"
print(s.isdigit())  # True

s = "abc"
print(s.isalpha())  # True

s = "abc123"
print(s.isalnum())  # True


# capitalize() & title()
s = "hello world"

print(s.capitalize())  # Hello world
print(s.title())       # Hello World


# String Reverse
s = "afroj"
print(s[::-1])



# Interview Tip
#  Ye functions sabse zyada use hote hain:
# 	•	split() 
# 	•	join()
# 	•	replace()
# 	•	strip()
# 	 •	find()