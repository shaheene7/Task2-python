
from abc import ABC, abstractmethod

class State(ABC):
  @abstractmethod
  def insert_coin(self, machine):
    pass
  
  @abstractmethod
  def select_product(self, machine):
    pass
  
  @abstractmethod
  def dispense(self, machine):
     pass
    
class IdleState(State):
  def insert_coin(self, machine):
    print("Coin inserted.")
    machine.set_state(HasMoneyState())
  
  def select_product(self, machine):
    print("Please insert coin first.")
  
  def dispense(self, machine):
     print("Insert coin and select product first.")

class HasMoneyState(State):
  def insert_coin(self, machine):
    print("Already has money.")
  
  def select_product(self, machine):
    print("Product selected. Dispensing...")
    machine.set_state(DispensingState())
  
  def dispense(self, machine):
    print("Select a product first.")


class DispensingState(State):
  def insert_coin(self, machine):
    print("Please wait, dispensing in progress.")
  
  def select_product(self, machine):
    print("Already dispensing. Please wait.")
  
  def dispense(self, machine):
    print("Product dispensed. Returning to idle state.")
    machine.set_state(IdleState())

class VendingMachine:
  def __init__(self):
    self.state = IdleState()
  
  def set_state(self, state):
    self.state = state
  
  def insert_coin(self):
    self.state.insert_coin(self)
  
  def select_product(self):
    self.state.select_product(self)
  
  def dispense(self):
    self.state.dispense(self)


vm = VendingMachine()

vm.insert_coin()       
vm.insert_coin()       
vm.select_product()    
vm.select_product()
vm.dispense()         
vm.dispense() 


"""each machine state is encapsulated in its own class, allowing state-specific behavior to be handled independently
making it easy to add new states without modifying existing logic."""