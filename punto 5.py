números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,13,100]
filtrados=list(filter(lambda x: x%2!=0, números))
print(filtrados)