#list comprehensions

even_numbers = [x for x in range(1,101) if x % 2==0]
print(even_numbers)

odd_numbers = [x for x in range(1,101) if x % 2!=0]
print(odd_numbers)
