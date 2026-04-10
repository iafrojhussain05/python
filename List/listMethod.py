names_list = ["Apple" , "Banana" , 1212 , 64.7647 , True , "Afroj"]

names_list.append("Raja Babu") # add data
print(names_list)

l1 = [2 ,7 ,2 ,9 ,5 , 3 ,4  ,1 , 9]
# l1.sort() # Shorting data 
# l1.reverse() # Reverse Data
# l1.insert(3 , "Aj") # insert function  using to insert data at Whatever index (specific position pe add)

# l1.extend([  "kya hai " , 123]) # multiple elements add
# l1.pop(3) #index se delete (default last)
# print(l1.pop(3)) 

# l1.remove(9) # remove data agar duble same data hai to first remove karega

# l1.sort()
# l1.sort(reverse=True) #Descending:
# l1.reverse() # reverse

# print(l1.index(9)) # find index using data
# print(l1.count(2)) # count() – kitni baar element aaya

copy_list = l1.copy() 
copy_list.clear()
print(l1)
print(copy_list)