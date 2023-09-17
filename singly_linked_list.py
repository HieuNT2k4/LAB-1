from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1
    def addToHead(self, x):  # Add Node to beg of linked list
        if self.head is None:
            self.head = x
        else:  # If Linked List empty , auto create new node
            x.next = self.head
            self.head = x

    # 2
    def addToTail(self, x):  # Add Node to end of linked list
        if self.head is None:
            self.head = x
        else:
            end = self.head
            while end.next is not None:
                end = end.next
            end.next = x
        # 3

    def addAfter(self, p, x):  # Add node x after node p
        new_node = Node(x)
        if p is None:
            return
        new_node.next = p.next
        p.next = new_node

        # 4

    def traverse(self):  # Traverse from head to tail
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

        # 5

    def deleteFromHead(self):  # Delete Head
        if self.head is None:
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node

        # 6
    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def deleteFromTail(self):
        if self.head is None:
            return None  # The list is empty

        if self.head.next is None:
            # If there's only one node in the list, delete it and return its data
            deleted_data = self.head.data
            self.head = None
            return deleted_data

        current = self.head
        while current.next.next is not None:
            current = current.next

        deleted_data = current.next.data
        current.next = None
        return deleted_data


        # 7

    def deleteAfter(self, p):  # Delete node after node p
        if p is None or p.next is None:
            return None
        deleted_node = p.next
        p.next = p.next.next
        return deleted_node.data

        # 8

    def delete(self, x):  # Delete the first node whose info is equal to x
        current = self.head
        previous = None
        while current:
            if current.data == x:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

        # 9

    def search(self, x):  # Return the reference to the first node having info x
        current = self.head
        position = 0
        while current:
            if current.data == x:
                return "Node position is:", position
            current = current.next
            position += 1

        # 10

    def count(self):  # Count and return the number of nodes in the list
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

        # 11

    def delete_ith(self, i):  # Delete the i-th node in the list
        if i < 0:
            return

        if i == 0:
            if self.head:
                self.head = self.head.next
            return

        current = self.head
        previous = None
        node_index = 0

        while current:
            if node_index == i:
                if current.next:
                    previous.next = current.next
                else:
                    previous.next = None
                return
            previous = current
            current = current.next
            node_index += 1

        # 12

    def sort(self): # Sort Ascending
        if self.head is None or self.head.next is None:
            return

        sorted_head = None  # Initialize the sorted list

        current = self.head
        while current is not None:
            next_node = current.next

            # Insert current node into the sorted list
            if sorted_head is None or current.data <= sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                current_sorted = sorted_head
                while current_sorted.next is not None and current.data > current_sorted.next.data:
                    current_sorted = current_sorted.next
                current.next = current_sorted.next
                current_sorted.next = current

            current = next_node

        self.head = sorted_head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

        # 13

    def del_exist_node(self, p):  # Delete existing node p
        current = self.head
        previous = None

        while current:
            if current.data == p:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                del current
                return

            previous = current
            current = current.next

        # 14

    def toArray(self):  # Return an array containing info of all nodes in the list
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

        # 16

    def addBefore(self, p, x):
        if self.head is None:
            return

        prev_node = self.get_prev_node(p)
        self.addAfter(prev_node, x)

        # 18

    def max(self):  # Detect maximum value
        if self.head is None:
            return None
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

        # 19

    def min(self):  # Detect minimum value
        if self.head is None:
            return None
        min_value = self.head.data
        current = self.head
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

        # 20

    def sum(self):  # Sum all values
        S = 0
        current = self.head
        while current:
            S += current.data
            current = current.next
        return S

        # 21

    def avg(self):  # Average of all values
        avg = 0
        if self.head is None:
            return avg

        sum_val = 0
        count = 0
        current = self.head
        while current:
            sum_val += current.data
            count += 1
            current = current.next
        if count != 0:
            avg = sum_val / count
        return avg

        # 22

    def is_sorted(self):  # Return True if the list is sorted
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

        # 23

    def insert(self, x):  # Insert node with value x into a sorted list so that the new list is sorted
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        if x <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.data < x:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    #25














