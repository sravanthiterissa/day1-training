#sets
#union
'''a={1,2,3,4}
b={2,3,5,6}
print(a.union(b))
print(a|b)'''
#intersection
'''a={1,2,3,4}
b={2,3,5,6}
print(a.intersection(b))
print(a&b)'''
#intersection update
'''a={1,2,3,4}
b={2,3,5,6}
print(a.intersection_update(b))
print(a)'''
#difference
'''a={1,2,3,4}
b={2,3,5,6}
print(a.difference(b))
print(a-b)'''
#symmetric difference
'''a={1,2,3,4}
b={2,3,5,6}
print(a.symmetric_difference(b))
print(a^b)'''
#difference update
'''a={1,2,3,4}
b={2,3,5,6}
a.difference_update(b)
print(a)'''
#symmetric difference update
a={1,2,3,4}
b={2,3,5,6}
a.symmetric_difference_update(b)
print(a)
