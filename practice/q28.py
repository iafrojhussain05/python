
# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter post : ")

if("harry".lower() in post.lower()):
    print("yes harry in this post")
else:
    print("no harry is not in this post")    