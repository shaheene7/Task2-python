from copy import deepcopy

class DrawingSnapshot:
    
    def __init__(self, shapes):
        self._state = tuple(shapes)

    def state(self):
        return self._state
    
class Drawing:

    def __init__(self):
        self._shapes = []

    def add_shape(self, shape):
        self._shapes.append(shape)

    def save(self):
        return DrawingSnapshot(deepcopy(self._shapes))
    
    def restore(self, snapshot: DrawingSnapshot):
        self._shapes = list(snapshot.state())

    def __str__(self):
        return f"Drawing: {self._shapes}"
    
def main():
    drawing = Drawing()
    drawing.add_shape("Circle")
    snap1 = drawing.save()

    drawing.add_shape("Square")
    snap2 = drawing.save()

    drawing.add_shape("Triangle")
    print(drawing)  

    drawing.restore(snap1)
    print(drawing)  

    drawing.restore(snap2)
    print(drawing)  

main()

""" it captures lightweight, immutable snapshots of an object’s state without exposing its internal details
     these snapshots enable restoring previous states safely and cleanly"""
