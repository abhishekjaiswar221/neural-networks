print("hebb rule")
w1 = [0, 0, 0, 0]
w2 = [0, 0, 0, 0]
s = [1, 0, 1, 0]
t = [1, 0]

print("W1 values")
w1new = []
for i in range(0, 4):
    newweight1 = w1[i] + s[i] * t[0]
    w1new.append(newweight1)
    print("old w1", (i + 1), "= ", w1[i], "| new w1", (i + 1), " = ", w1new[i])

print("W2 values")
w2new = []
for i in range(0, 4):
    newweight2 = w2[i] + s[i] * t[1]
    w2new.append(newweight2)
    print("old w2", (i + 1), " = ", w2[i], "| new w2", (i + 1), " = ", w2new[i])

w1 = w1new
w2 = w2new

print("The final weight matrix is : ")
print("W = ")
for i in range(0, 4):
    print(w1[i], w2[i])

print("Done")
