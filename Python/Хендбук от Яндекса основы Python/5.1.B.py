class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, sec_p):
        res = round(((self.x - sec_p.x) ** 2 + (self.y - sec_p.y) ** 2) ** (1 / 2), 2)
        return res
    

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))