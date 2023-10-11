lst = [1,4,7,3]
result = list(map(lambda x: x**2, lst))

print(result)

result2 = [i for i in lst if i % 2 == 0]
print(result2)

lst2 = [(1, "c"), (2, "b"), (3, "a")]
lst2.sort(key=lambda i: i[1])
print(lst2)
















