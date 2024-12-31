list1=[1,2,3,4,True,"Sachin"]
print(list1)
print(list1[0])
print(list1[0:])
print(list1[:])

#same goes for strings also
if 4 in list1:
    print("Yes")
else:
    print("No")

if "Sa" in list1:
    print("Yes")
else:
    print("No")

list2=[i for i in range(10)]
print(list2)

list3=[i*i for i in range(10) if i%2==0]
print(list3)