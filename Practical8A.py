print("overlap in operator")

list1=[12,23,45,67,80]
list2=[34,45,66,78,90]

flag=0
for i in list1:
    if i in list2:
        flag=1

if(flag==1):
   print("The Lists Overlap")
else:
   print("The Lists do Not overlap")
