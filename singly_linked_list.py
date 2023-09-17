from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1
    def addToHead(self, x):  #Add Node to beg of linked list
        if self.head is None:
            self.head = x
        else:   #If Linked List empty , auto create new node
            x.next = self.head
            self.head = x

    # 2
    def addToTail(self, x):  #Add Node to end of linked list
        if self.head is None:
            self.head = x
        else:
            end = self.head
            while end.next is not None:
                end = end.next
            end.next = x

    # 3
    def addAfter(self, p, x):  # Add node x after node p
        x.next = p.next
        p.next = x

    # 4
    def traverse(self): #Traverse from head to tail
        node = self # 1st Node / Head Node
        while node != Node:
            node = node.next  # Next node
        return node

    #5
    def deleteFromHead(self): # Delete Head
        node = self
        if node is None:
            self.head = self.head.next
        else:
            node = node.next
        return node


    #6
    def get_prev_node(self, node):
        current = self.head
        while (current and current.next != node):
            current = current.next
        return current

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def deleteFromTail(self, node):  # Delete Tail
        prev_node = self.get_prev_node(node)
        if prev_node is not None:
            prev_node.next = node.next
        return prev_node

    # 7
    def deleteAfter(self, p): #Delet node after node p
        if p is None or p.next is None:
            return None  # Node p is None or p is the last node

        deleted_node = p.next  # The node to be deleted
        p.next = p.next.next

        return deleted_node.data

    # 8
    def delete(self, x): # Delele the first node whose info is equal to x
        node = self.head
        while node:
            current = node
            node = node.next
            if node == x:
                current = current.next
                break

    # 9
    def search(self, x): #Return the reference to the first node having info x
        node = self.head
        while node:
            if node == x:
                return node
            node = node.next
        return None

    # 10
    def count(self): #Count and return number of nodes in the list
        node = self.head
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    # 11
    def delete_ith(self, i): #Delete an i-th node on the list
        if i < 0:
            return

        if i == 0:
            if self.head:
                self.head = self.head.next
            return

        node = self.head
        previous = None
        node_index = 0

        while node:
            if node_index == i:
                if node.next:
                    previous.next = node.next
                else:
                    previous.next = None
                return
            previous = node
            node = node.next
            node_index += 1

    #12
    def sort(self):
        if not self.head:
            return

        node = self.head
        prev_node = self.get_prev_node(node)
        while node:
            node = node.next
            if node > prev_node:
                node = prev_node
                prev_node = node
            else:
                node = node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()















