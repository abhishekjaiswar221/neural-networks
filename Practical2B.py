# B] Generate XOR function using McCulloch-Pitts neural net.
# Code :
print("Name: Abhishek Jaiswar")
print("Roll No.: 3")
print("XOR function using Mc-Culloch Pitts neuron")
x1inputs = [1, 1, 0, 0]
x2inputs = [1, 0, 1, 0]

print("Calculating z1 = x1 x2'")

print("Considering one weight as excitatory and other as inhibitory.")

w1 = [1, 1, 1, 1]
w2 = [-1, -1, -1, -1]

z1 = []

print("x1 ", "x2 ", "z1")
for i in range(0, 4):
    z1.append(x1inputs[i] * w1[i] + x2inputs[i] * w2[i])
    print(x1inputs[i], " ", x2inputs[i], " ", z1[i])

print("Calculating z2 = x1' x2")

print("Considering one weight as excitatory and other as inhibitory.")

w1 = [-1, -1, -1, -1]
w2 = [1, 1, 1, 1]

z2 = []

print("x1 ", "x2 ", "z2")

for i in range(0, 4):
    z2.append(x1inputs[i] * w1[i] + x2inputs[i] * w2[i])
    print(x1inputs[i], " ", x2inputs[i], " ", z2[i])

print("Applying Threshold=1 for z1 and z2")

print("z1 ", "z2")
for i in range(0, 4):
    if (z1[i] >= 1):
        z1[i] = 1
    else:
        z1[i] = 0

    if (z2[i] >= 1):
        z2[i] = 1
    else:
        z2[i] = 0
    print(z1[i], " ", z2[i])

y = []
v1 = 1
v2 = 1
print("x1", "x2", " y")
for i in range(0, 4):
    y.append(z1[i] * v1 + z2[i] * v2)
    print(x1inputs[i], " ", x2inputs[i], " ", y[i])
