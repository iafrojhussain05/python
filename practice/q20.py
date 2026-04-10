# Create an empty dictionary. Allow 4 friends to enter their favorite language as alue and use key as their names. Assume that the names are unique.

d = {}

friends_name = input("Enter Friend Name : ")
fav_lang = input("Enter favorite language : ")
d.update({friends_name: fav_lang})

friends_name = input("Enter Friend Name : ")
fav_lang = input("Enter favorite language : ")
d.update({friends_name: fav_lang})

friends_name = input("Enter Friend Name : ")
fav_lang = input("Enter favorite language : ")
d.update({friends_name: fav_lang})

print(d)

# If the names of 2 friends are same; what will happen to the program in problem 6?
# updated value print


# If languages of two friends are same; what will happen to the program in problem 6?
# print given language not change