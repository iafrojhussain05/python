name = 'Hello'
age = "20"
cource = '''BCA'''

print(name,age,cource)

# len() fuction use to find number of length
print("Length of String (name) :",len(name)) 

# access using index in string
print(name[3])

short_name = name[0:4] # 0 index to 3 index 
print(short_name)
print(name[0:]) # means 0 index to last index
print(name[:4]) # starting index to 3rd index

# Negative indexing
name_n = name[-5:-1] #
print(name_n)


str_list = "hello"

print(str_list.replace("h" ,"H" ))
