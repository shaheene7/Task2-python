class Shape(object):
    
    def __init__(self, *args, **kwargs):
        pass

    def render(self):
        pass

class Circle(Shape):
    
    def __init__(self, name):
        super().__init__()
        self.name = name

    def render(self):
         print(f"Circle: {self.name}")

class ShapeGroup(Shape):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.children = []

    def add(self, shape):
        self.children.append(shape)

    def remove(self, shape):
        self.children.remove(shape)

    def render(self):
        print(f"Group: {self.name}")
        for child in self.children:
            child.render()


group1 = ShapeGroup("Group1")
circle1 = Circle("Circle1")
circle2 = Circle("Circle2")
group1.add(circle1)
group1.add(circle2)

circle3 = Circle("Circle3")

main_group = ShapeGroup("MainGroup")
main_group.add(group1)
main_group.add(circle3)

main_group.render()


""" it allows individual shapes and groups of shapes to be treated uniformly through a common interface 
    this lets client code interact with simple and complex objects"""