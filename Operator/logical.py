#Logical Operator 

#Types: and , or , not 

a = 10
b = 20


# and : both value are true = true otherwise false
print("and Operator :")
print((a>b) and (a<b)) # false
print((a<b) and (a<b)) # true

# or : both value are false = false otherwise true
print("or Operator :")
print((a>b) or (a<b)) # true
print((a>b) or (a==b)) # false

# not : oposite 
print("not Operator :")
print(not(a==b))
print(not(a<b))

