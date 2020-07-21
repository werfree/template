class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.cur = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.cur = new_node
        else:
            self.cur.next = new_node
            self.cur = new_node
        print("Push",new_data)

    def display(self):
        print("Display:- ", end="")
        if self.head is None:
            print("LinkedList is Empty.")
        else:
            temp = self.head
            print(temp.data, "-> ", end="")
            while temp.next is not None:
                temp = temp.next
                print(temp.data, "-> ", end="")
        print("None")

    def length(self):
        if self.head is None:
            count = 0
        else:
            count = 1
            temp = self.head
            while temp.next is not None:
                count += 1
                temp = temp.next
        print("Length = ", count)


linkList = LinkedList()
linkList.length()
linkList.display()
linkList.push(1)
linkList.push(2)
linkList.push(1)
linkList.push(2)
linkList.push(1)
linkList.push(2)
linkList.display()

