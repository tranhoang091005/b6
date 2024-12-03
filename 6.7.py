print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return math.pi * self.radius **  2

    def circumference(self):
        return 2 * math.pi * self.radius

radius = float(input("Nhập bán kính hình tròn: "))
circle = Circle(radius)
print(f"Diện tích hình tròn: {circle.area():.2f}")
print(f"Chu vi hình tròn: {circle.circumference():.2f}")
