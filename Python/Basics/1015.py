import math

x1, y1 = [float(x) for x in input("Enter two value: ").split()]
x2, y2 = [float(x) for x in input("Enter two value: ").split()]

R = math.sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))

print ("%.4f" % R)
