# 8. Wap to findout volume,cost and weight of a box using multilevel inheritance with and without super keyword?
# Without using super keyword
class Shape:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self):
        return self.length * self.width * self.height


class Box(Shape):
    def __init__(self, length, width, height, cost):
        Shape.__init__(self, length, width, height)
        self.cost = cost

    def calculate_cost(self):
        volume = self.calculate_volume()
        return volume * self.cost


class WeightedBox(Box):
    def __init__(self, length, width, height, cost, weight):
        Box.__init__(self, length, width, height, cost)
        self.weight = weight

    def calculate_weight(self):
        return self.weight


# Using super keyword
class Shape:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self):
        return self.length * self.width * self.height


class Box(Shape):
    def __init__(self, length, width, height, cost):
        super().__init__(length, width, height)
        self.cost = cost

    def calculate_cost(self):
        volume = self.calculate_volume()
        return volume * self.cost


class WeightedBox(Box):
    def __init__(self, length, width, height, cost, weight):
        super().__init__(length, width, height, cost)
        self.weight = weight

    def calculate_weight(self):
        return self.weight


# Without using super keyword
print("Without using super keyword")
length = float(input("Enter the length of the box: "))
width = float(input("Enter the width of the box: "))
height = float(input("Enter the height of the box: "))
cost = float(input("Enter the cost per unit volume: "))
weight = float(input("Enter the weight of the box: "))

box1 = WeightedBox(length, width, height, cost, weight)

volume = box1.calculate_volume()
cost = box1.calculate_cost()
weight = box1.calculate_weight()

print("Volume:", volume)
print("Cost:", cost)
print("Weight:", weight)


# Using super keyword
print("\nWith using super keyword")
length = float(input("Enter the length of the box: "))
width = float(input("Enter the width of the box: "))
height = float(input("Enter the height of the box: "))
cost = float(input("Enter the cost per unit volume: "))
weight = float(input("Enter the weight of the box: "))

box2 = WeightedBox(length, width, height, cost, weight)

volume = box2.calculate_volume()
cost = box2.calculate_cost()
weight = box2.calculate_weight()

print("Volume:", volume)
print("Cost:", cost)
print("Weight:", weight)
