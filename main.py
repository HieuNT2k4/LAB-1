from node import Node
from singly_linked_list import SinglyLinkedList

a_llist = SinglyLinkedList()

print()
print('             Menu')
print('--------------------------------')
print('   - insert at beg')
print('   - insert at end')
print('   - insert after <index>')
print('   - delete at beg')
print('   - delete at end')
print('   - delete after <index>')
print('   - delete first node')
print('   - delete at <index> ')
print('   - delete exist <index>')
print('   - quit')

while True:
    print('The list: ')
    a_llist.display()
    print()

    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()

    if operation == 'insert':
        suboperation = do[1].strip().lower()
        position = do[2].strip().lower()
        if suboperation == 'at':
            if position == 'beg':
                name = input('   - Enter name: ')
                salary = float(input('   - Enter salary: '))
                a_llist.addToHead(Node([name, salary]))
            elif position == 'end':
                name = input('   - Enter name: ')
                salary = float(input('   - Enter salary: '))
                a_llist.addToTail(Node([name, salary]))
            elif isinstance(position, int):
                a_llist.delete_ith(position)

        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                name = input('   - Enter name: ')
                salary = float(input('   - Enter salary: '))
                a_llist.addAfter(ref_node, Node([name, salary]))


    elif operation == 'traverse':
        a_llist.traverse()

    elif operation == 'search':
        name = input('   - Enter name: ')
        a_llist.search(name)

    elif operation == 'count':
        a_llist.count()

    elif operation == 'sort':
        a_llist.sort()

    elif operation == 'delete':
        suboperation = do[1].strip().lower()
        position = do[2].strip().lower()
        if suboperation == 'at':
            if position == 'beg':
                a_llist.deleteFromHead()
            elif position == 'end':
                index = int(position)
                prev_node = a_llist.get_prev_node(index)
                a_llist.deleteFromTail(prev_node)

        elif suboperation == 'exist':
            position = do[2].strip().lower()
            a_llist.del_exist_node(position)


        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_llist.deleteAfter(ref_node)

    elif do == 'delete first node':
        first_node = a_llist.get_node(0)
        a_llist.delete(first_node)


    elif operation == 'quit':
        break
