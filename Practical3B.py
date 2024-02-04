import math

print("Delta")
print("Using 3 inputs 3 weights 1 output.")
x1 = [0.3, 0.5, 0.8]  # inputs
w1 = [0.1, 0.1, 0.1]  # weights
t = 1  # TARGET
a = 0.1  # alpha
diff = 1  # initial difference
yin = 0  # initial net input

while diff > 0.4:

    for i in range(0, 3):
        yin = yin + (x1[i] * w1[i])

    yin = round(yin + 0.25, 3)
    print("Yin = ", yin, "target = ", t)
    diff = t - yin
    diff = math.fabs(round(diff, 3))
    print("error = ", diff)
    neww1 = []
    for i in range(0, 3):  # update weights
        w1new = round(w1[i] + a * diff * x1[i], 2)
        neww1.append(w1new)
    print("w1new = ", neww1)
    w1 = neww1
    print("")
