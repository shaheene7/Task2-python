import abc

class Button(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

class ScrollBar(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

class Windows:
    def drawButton(self):
        return "Drawing a Windows button"
    
    def drawScrollBar(self):
        return "Drawing a Windows scrollbar"
    
class MacOS:
    def drawButton(self):
        return "Drawing a MacOS button"
    
    def drawScrollBar(self):
        return "Drawing a MacOS scrollbar"
    
class Linux:
    def drawButton(self):
        return "Drawing a Linux button"
    
    def drawScrollBar(self):
        return "Drawing a Linux scrollbar"
    
class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def createButton(self):
        pass
        
    @abc.abstractmethod
    def createScrollBar(self):
        pass
    
class WindowsFactory(AbstractFactory):
    def createButton(self):
        return Windows().drawButton()
    
    def createScrollBar(self):
        return Windows().drawScrollBar()        

class MacOSFactory(AbstractFactory):    
    def createButton(self):
        return MacOS().drawButton()
    
    def createScrollBar(self):
        return MacOS().drawScrollBar()  

class LinuxFactory(AbstractFactory):
    def createButton(self):
        return Linux().drawButton()
    
    def createScrollBar(self):
        return Linux().drawScrollBar()



windows = WindowsFactory()
print(windows.createButton())  
print(windows.createScrollBar())  

mac = MacOSFactory()
print(mac.createButton())  
print(mac.createScrollBar())  



"""it can provide a way to create families of realted widgets for different OS
    each OS has its own factory """