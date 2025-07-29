from abc import ABC, abstractmethod
import time     
import asyncio

class OrderHandler():
    
    def process(self, order):
        raise NotImplemented

class BaseProcessor(OrderHandler):

    def process(self,order):
        print(f"Processing order {order.order_id} for user {order.user.name}")
        time.sleep(0.5)
        order.status = "Processed" 

class ValidationProcessor(OrderHandler):
    
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def process(self, order):
        print(f"[VALIDATE] Checking order {order.order_id}...")
        if order.status != "Pending":
            raise Exception("Order already processed or invalid status")
        self.wrapper.process(order)
       
class LoggingProcessor(OrderHandler):
    
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def process(self,order):
        order.status = "Pending"
        print(f"[LOG] Starting process {order.order_id}...")
        self.wrapper.process(order)
        print(f"[LOG] Finished process {order.order_id}.")
        
class User:
     def __init__(self, name): 
        self.name = name 
        self.notification_channels = []

     
     def subscribe_channel(self, channel):
        if channel not in self.notification_channels:
            self.notification_channels.append(channel)

     def unsubscribe_channel(self, channel):
        if channel in self.notification_channels:
            self.notification_channels.remove(channel)
        else:
             print(f"{channel} not found in subscribed channels for {self.name}")
            
class Order: 
    
    def __init__(self, order_id, user):
       self.order_id = order_id 
       self.user = user 
       self.status = "Created" 
              
class OrderProcessor:
    
     def __init__(self): 
        self.history = [] 
        self.redo_stack = [] 
        self.logger = Logger(level="DEBUG")
        
     async def process_order(self, order):
        processor = LoggingProcessor(ValidationProcessor(BaseProcessor()))
        processor.process(order)
        print(f"Processing complete for order {order.order_id} (User: {order.user.name})")
        await self.send_notifications(order)
        
        
     def change_status(self, order, new_status):
        status = StatusChangeCommand(order, order.status, new_status)
        status.redo() 
        self.history.append(status)
        self.redo_stack.clear()
         
     def undo_status(self): 
        if self.history:
            status = self.history.pop()
            status.undo()
            self.redo_stack.append(status)
        else:
            print("Nothing to undo") 
        
     def redo_status(self): 
        if self.redo_stack:
            status = self.redo_stack.pop()
            status.redo()
            self.history.append(status)
        else:
            print("Nothing to redo")
        
     async def send_notifications(self, order): 
        user = order.user 
        msg = f"Your order {order.order_id} is now {order.status}" 
        for channel in user.notification_channels:
            await channel.send(user, msg)
         
        
     def log(self, message, level): 
          self.logger.log(level, message)
      
class StatusChangeCommand:
    def __init__(self, order, from_status, to_status):
        self.order = order
        self.from_status = from_status
        self.to_status = to_status

    def undo(self):
        self.order.status = self.from_status
        print(f"Undo: Order {self.order.order_id} status reverted to {self.from_status}")

    def redo(self):
        self.order.status = self.to_status
        print(f"Redo: Order {self.order.order_id} status changed to {self.to_status}")

class Logger:
    levels = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}

    def __init__(self, level="DEBUG"):
        self.current_level = self.levels[level]

    def log(self, level, message ):
        if self.levels[level] >= self.current_level:
          print(f"[{level}] {time.strftime('%H:%M:%S')}: {message}")
         
class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, user, msg): pass

class EmailNotification(NotificationStrategy):
    async def send(self, user, msg):
        await asyncio.sleep(0.1)
        print(f"[Email] Sent to {user.name}: {msg}")

    def __str__(self):
        return "EmailNotification"

class SMSNotification(NotificationStrategy):
    async def send(self, user, msg):
        await asyncio.sleep(0.1)
        print(f"[SMS] Sent to {user.name}: {msg}")

    def __str__(self):
        return "SMSNotification"

class PushNotification(NotificationStrategy):
   async def send(self, user, msg):
        await asyncio.sleep(0.1)
        print(f"[Push] Sent to {user.name}: {msg}")

   def __str__(self):
        return "PushNotification"

class OrderFacade:
    def __init__(self):
        self.processor = OrderProcessor()
    
    async def place_order(self, order):
        await self.processor.process_order(order)
    
    def change_order_status(self, order, new_status):
        self.processor.change_status(order, new_status)
        
    def undo(self):
        self.processor.undo_status()
    
    def redo(self):
        self.processor.redo_status()


async def main(): 
    
    user = User("Bob") 
    push = PushNotification()
    email = EmailNotification()
    sms = SMSNotification()
    user.subscribe_channel(email)
    user.subscribe_channel(sms)
    user.unsubscribe_channel(push)
    order = Order(1001, user) 
    facade = OrderFacade()
    await facade.place_order(order)
    facade.change_order_status(order, "Shipped")
    facade.undo()
    facade.redo()
    
if __name__ == "__main__": 
   asyncio.run(main())  