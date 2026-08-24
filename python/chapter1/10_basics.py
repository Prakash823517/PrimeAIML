import math
def circle_stats(radius):
    return math.pi * radius ** 2

print(circle_stats(2))

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle(3)

print("Area:", a)
print("Circumference: ",c)