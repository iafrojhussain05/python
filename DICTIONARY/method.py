marks = {
    "key": "Value",
    "Afroj": 87,
    "Raja": 67,
    "Rohan": 70
      
}

# print(marks["Afroj"] , type(marks))
# print(marks.items())
# print(marks.keys())
# print(marks.values())

#Update method
marks.update({"Afroj": 85 , "Salman": 60})
# print(marks)

# get method
print(marks.get("Afroj")) # print none
print(marks["Afroj"]) # Error 

s = {} # Empty dictionary 

print(len(marks))
