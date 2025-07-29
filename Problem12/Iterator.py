
class Feed:

    def __init__(self):
        self._items = ["post1", "ad1", "suggested1", "post2"]

    def get_chrono_iterator(self):
        return iter(self._items)
    
    def get_unread_iterator(self):
        return (item for item in self._items if "post" in item)

    def get_popular_iterator(self):
        popular_order = ["post2", "post1", "ad1", "suggested1"]
        return (item for item in popular_order if item in self._items)




feed = Feed()

print("Chronological:")
for item in feed.get_chrono_iterator():
    print(item)

print("\nUnread:")
for item in feed.get_unread_iterator():
    print(item)

print("\nMost Popular:")
for item in feed.get_popular_iterator():
    print(item)

"""it hides the internal structure of the feed while providing standardized ways to traverse its items 
    new traversal orders can be added independently without modifying the Feed class"""