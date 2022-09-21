list1=[]
list2=[]
n=int(input("enter the number of elements: "))
for i in range(0,n):
    el=int(input())
    list1.append(el)
for j in range(0,n):
    if list1[j]>0:
        list2.append(list1[j])
print(list2)
