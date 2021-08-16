from math import hypot
co = float(input("Cateto oposto: ".strip()))
ca = float(input("Cateto adjacente: ".strip()))
hi = hypot(co, ca)
hi2= round(hi, 2)
print(hi2)
