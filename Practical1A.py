print("Name: Abhishek Jaiswar")
print("Roll No. 3")
n = int(input("Enter the number of inputs:"))
yin = 0
for i in range(n):
    x = float(input("Enter x :"))
    w = float(input("Enter weight:"))
    yin = yin + x * w

print("Yin=", yin)

if yin < 0:
    output = 0
elif yin > 1:
    output = 1
else:
    output = yin
