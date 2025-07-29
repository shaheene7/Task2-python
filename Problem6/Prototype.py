import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj
    

class NPC:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def __str__(self):
        return f"(Name: {self.name}, weapon: {self.weapon})"
    
npc1 = NPC("Goblin", {"type": "Axe", "damage": 10})
prototype = Prototype()
prototype.register_object("Goblin", npc1)
npc2 = prototype.clone("Goblin")   

npc3 = prototype.clone("Goblin", weapon={"type": "Sword", "damage": 20})
print(npc3)

print(npc2) 
npc2.weapon["damage"] = 15
print(npc2) 
print(npc1)


"""it lets each game object define its own cloning logic, 
   avoiding the need for a centralized
   composite fields are safely duplicated."""


    
