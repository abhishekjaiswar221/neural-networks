# A] Generate AND/NOT function using McCulloch-Pitts neural net.
# Code :
print("Name: Abhishek Jaiswar")
print("Roll No.: 3")
print("AND NOT function using Mc Culloch Pitts")
x1inputs = [1, 1, 0, 0]
x2inputs = [1, 0, 1, 0]

print("Considering all weights as excitatory.")

w1 = [1, 1, 1, 1]
w2 = [1, 1, 1, 1]

y = []

print("x1", " x2", " y")
for i in range(0, 4):
    y.append(x1inputs[i] * w1[i] + x2inputs[i] * w2[i])
    print(x1inputs[i], " ", x2inputs[i], " ", y[i])

print("Considering one weight as excitatory and other as \ninhibitory.")

w1 = [1, 1, 1, 1]
w2 = [-1, -1, -1, -1]

y = []

print("x1", " x2 ", "y")
for i in range(0, 4):
    y.append(x1inputs[i] * w1[i] + x2inputs[i] * w2[i])
    print(x1inputs[i], " ", x2inputs[i], " ", y[i])

print("Applying Threshold = 1")

Y = []
print("x1 ", "x2 ", "Y")
for i in range(0, 4):
    if y[i] >= 1:
        value = 1
        Y.append(value)
    else:
        value = 0
        Y.append(value)
    print(x1inputs[i], " ", x2inputs[i], " ", Y[i])
