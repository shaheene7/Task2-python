from abc import ABC, abstractmethod
from typing import Optional, Tuple

class Handler(ABC):
    def __init__(self, successor: Optional['Handler'] = None):
        self.successor = successor

    def handle(self, request):
        if not self.check_range(request):
            return False
        if self.successor:
            return self.successor.handle(request)
        return True
        

    @abstractmethod
    def check_range(self, request):
        pass


class AuthHandler(Handler):

 
    def check_range(self,request):
        if not request.get("auth"):
            print("Auth failed")
            return False
        return True
    

class RateLimitHandler(Handler):

    def check_range(self,request):
        if request.get("rate") > 100:
            print("Rate limit exceeded")
            return False
        return True
    

class VirusScanHandler(Handler):
  
    def check_range(self,request):
        if "virus" in request.get("content"):
            print("Virus detected")
            return False
        return True
    


handler_chain = AuthHandler(
    RateLimitHandler(
        VirusScanHandler()
    )
)

req = {
    "auth": True,
    "rate": 100,
    "content": " text"
}

print("Validation result:", handler_chain.handle(req))


"""it decouples request processing by passing it through a chain of independent handlers, 
    each responsible for a specific check."""