'''Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 5 subjects and take marks as an input from the user. '''


#Subjects math , science , social science , English , Computer 

math = int(input("Enter maths number : "))

science = int(input("Enter Science number : "))

social_science = int(input("Enter Social Science number : "))

english = int(input("Enter English number : "))

computer = int(input("Enter Computer number : "))

total_percentage = (math + science + social_science + english + computer)/5
# total_percentage = (100*(math + science + social_science + english + computer))/500

if(total_percentage >= 40 and math >= 33 and social_science >= 33 and science >= 33 and computer >= 33 and english >= 33):
    print(f"congratulations You are Pass With {total_percentage} percentage " )

else:
    print(f"Sorry you are Fail your percentage {total_percentage}")    


