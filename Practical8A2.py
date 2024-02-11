print("not in")

list1=[23,56,78,90,89]
list2=[23,66,90,24,55]
flag=0
print("The elements in the first list not in second list are")
for i in list1:
    if i not in list2:
        print(i)
