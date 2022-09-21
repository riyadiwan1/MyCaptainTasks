
n = int(input("input the number of terms: "))
a,b,=0,1
print(a)
print(b)
for i in range(n):

    c = a + b
    print(c)
    a = b
    b = c
