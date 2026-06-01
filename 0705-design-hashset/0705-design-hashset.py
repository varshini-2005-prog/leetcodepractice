class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyHashSet:

    def __init__(self):
        self.head = None

    def add(self, key: int) -> None:

        if self.contains(key):
            return

        new = Node(key)

        if not self.head:
            self.head = new
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new

    def remove(self, key: int) -> None:

        if not self.head:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:

            if temp.next.data == key:
                temp.next = temp.next.next
                return

            temp = temp.next

    def contains(self, key: int) -> bool:

        temp = self.head

        while temp:

            if temp.data == key:
                return True

            temp = temp.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)