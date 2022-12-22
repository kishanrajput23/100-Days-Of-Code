countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
print(res)

res = tuple1.index(3)
print(res)

# res = tuple1.index(311)
res = tuple1.index(3, 4, 8)
print(res)

res = len(tuple1)
print('Count of 3 in tuple1 is:', res)
