from typing import List 

class Command:
    def __init__(self, name: str ):
        self.name = name

    def execute(self):
        print(f"Executing: {self.name}")

    def undo(self):
        print(f"Undoing command: {self.name}")

class MacroCommand(Command):
    def __init__(self, name: str, commands: List[Command]):
        super().__init__(name)
        self.commands = commands

    def execute(self):
        print(f"Executing macro: {self.name}")
        for cmd in self.commands:
            cmd.execute()

    def undo(self):
        print(f"Undoing macro: {self.name}")
        for cmd in reversed(self.commands):
            cmd.undo()

class CommandManager:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def add_command(self, command: Command):
        command.execute()
        self._undo_stack.append(command)
        self._redo_stack.clear()    

    def undo(self):
        if self._undo_stack:
            cmd = self._undo_stack.pop()
            cmd.undo()
            self._redo_stack.append(cmd)
        else:
            print("No commands to undo.")

    def redo(self):
        if self._redo_stack:
            cmd = self._redo_stack.pop()
            cmd.execute()
            self._undo_stack.append(cmd)
        else:
            print("No commands to redo.")

cmd1 = Command("Command 1")
cmd2 = Command("Command 2")
macro = MacroCommand("Macro 1", [cmd1, cmd2])

manager = CommandManager()
manager.add_command(cmd1)
manager.add_command(cmd2)
manager.undo()
manager.redo()

manager.add_command(macro)
manager.undo()
manager.redo() 


""" it encapsulates all user actions as objects with uniform execute, redo and undo methods
     makes it easy to implement multi-level undo/redo by"""

