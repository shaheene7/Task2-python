
class ChatRoom:

    def __init__(self):
        self.users = []

    def register(self, user):
        if user not in self.users:
            self.users.append(user)
            user.chat_room = self

    def broadcast(self, message, sender):
        for user in self.users:
            if user is not sender:
                user.display_message(sender, message)

    


class User:

    def __init__(self, name):
        self.name = name
        self.chat_room =  None

    def say(self, message):
        if self.chat_room:
            self.chat_room.broadcast(message, self)

    def display_message(self, user, message):
        print(f"{user} says: {message}")

    
    def __str__(self):
        return self.name
    


def main():
    chat_room = ChatRoom()

    molly = User("Molly")
    john = User("John")

    chat_room.register(molly)
    chat_room.register(john)




    molly.say("Hello, everyone!")
    

main()


"""which centralizes communication through a ChatRoom mediator so
 that components (like users or chat clients) do not communicate with each other directly
 making it easier to add, remove, or modify components without impacting others."""