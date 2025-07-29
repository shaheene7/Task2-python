class Observer:
    def __init__(self):
       self._observers = []

    def register_observer(self, observer):
        if observer not in self._observers:
          self._observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self._observers:
          self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
              observer.update(self)

class Core(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def upload_file(self, filename):
        self.filename = filename
        print(f"{self.name} uploaded {self.filename}")
        self.notify_observers()
        

class EmailSender:
    def update(self, core):
         print(f"Email sent to {core.name} confirming upload of {core.filename}")

class Logger:
    def update(self, core):
       print(f"[LOG] {core.name} uploaded {core.filename}")

class Dashboard:
    def update(self, core):
        print(f"Dashboard updated for {core.name}")
    

def main():
    core = Core("alice")
    emailer = EmailSender()
    logger = Logger()
    dashboard = Dashboard()

    core.register_observer(emailer)
    core.register_observer(logger)
    core.register_observer(dashboard)

    core.upload_file("report.pdf")
    core.upload_file("design.png")

main()


"""making it easy to add or remove subscribers
    and want to notify multiple independent components"""