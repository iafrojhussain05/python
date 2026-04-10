s = {1,1,2,3,4,5,6,7,3}

s.add(25)# add value
print(s) 

print(len(s))

s.remove(4) # remove data 
print(s)

s.pop() # randon data remove
print(s)

s1 = {1,2,3,4,5}
s2 = {6,7,8,1,9,10}
print(s1.union(s2))
print(s1.intersection(s2))