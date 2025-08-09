# Here we will be unpacking tuples

tup = [(1,2,3),(2,3,5),(4,6,7)]

# This for loop unpacks the list/tuple called tup and assigns the 'a' to the first index od each tuple then
# 'b' to the second and so on...
for a, b, c, in tup:
    print(f'a = {a}, b = {b}, c = {c}\n')
