a, b, c = 5, 6, 7
temp_b = b
temp_c = c
b = a
c = temp_b
a = temp_c
print(a, b, c, sep="\n")