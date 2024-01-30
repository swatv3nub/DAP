#using clear
lst = [1, 2, 3, 4, 5]
lst.clear()
print(lst)

#reassigning
lst = [1, 2, 3, 4, 5]
lst = []
print(lst)

#using del
lst = [1, 2, 3, 4, 5]
del lst[:]
print(lst)

#slicing
lst = [1, 2, 3, 4, 5]
lst[:] = []
print(lst)

#using *=
lst = [1, 2, 3, 4, 5]
lst *= 0
print(lst)