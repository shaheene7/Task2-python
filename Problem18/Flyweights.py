class CharacterFlyweights:
    
    def __init__(self, font, size, char):
        self.font = font
        self.size = size
        self.char = char
        
    def render(self, position):
        print(f"Render {self.char} in {self.font} {self.size}pt at position {position}")


class CharacterFactory:

    def __init__(self):
        self.flyweights = {}

    def getchar(self, char, font, size):
        key = (char, font, size)
        if key not in self.flyweights:
            self.flyweights[key] = CharacterFlyweights(font, size, char)

        return self.flyweights[key]
    

def main():
    factory = CharacterFactory()
    text = "hello world"
    font = "Arial"
    size = 12

    for i, c in enumerate(text):
        char = factory.getchar(c, font, size)
        char.render(i)

main()

"""it shares common, intrinsic data (like font and size) across many Character objects, minimizing memory usage
   allowing many lightweight flyweight instances to represent numerous characters efficiently """