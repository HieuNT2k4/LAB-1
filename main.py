from node import Node
from singly_linked_list import SinglyLinkedList

a_llist = SinglyLinkedList()

print()
print('             Menu')
print('--------------------------------')
print('   - insert <data> at beg')
print('   - insert <data> at end')
print('   - insert <data> after <index>')
print('   - insert <data> into sorted list')
print('   - insert <data> before <index>')
print('   - delete at beg')
print('   - delete at end')
print('   - delete after <index>')
print('   - delete first node')
print('   - delete at <index> ')
print('   - delete exist <index>')
print('   - search <data>')
print('   - count')
print('   - sort')
print('   - sorted')
print('   - array')
print('   - maximum value')
print('   - minimum value')
print('   - sum')
print('   - avg')
print('   - quit')

while True:
    print('The list: ', end = '')
    a_llist.display()
    print()

    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()

    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower()
        if suboperation == 'at':
            if position == 'beg':
                a_llist.addToHead(new_node)
            elif position == 'end':
                a_llist.addToTail(new_node)
        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_llist.addAfter(ref_node, new_node)
            elif suboperation == 'before':
                a_llist.addBefore(ref_node, new_node)

    elif operation == 'delete':
        suboperation = do[1].strip().lower()

        if suboperation == 'at':
            position = do[2].strip().lower()

            if position == 'beg':
                a_llist.deleteFromHead()
            elif position == 'end':
                last_node = a_llist.get_node(-1)
                a_llist.deleteFromTail(last_node)
            else:
                index = int(position)
                ref_node = a_llist.get_node(index)

                if ref_node is None:
                    print('No such index.')
                    continue

                a_llist.deleteAfter(ref_node)

        elif suboperation == 'exist':  # New suboperation for deleting by data
            data_to_delete = int(do[2])

            if a_llist.search(data_to_delete):
                a_llist.del_exist_node(data_to_delete)
            else:
                print('Data not found in the list.')



    elif operation == 'traverse':
        a_llist.traverse()

    elif operation == 'search':
        data = int(do[1])
        a_llist.search(data)
        print(a_llist.search(data))

    elif operation == 'count':
        print(a_llist.count())

    elif operation == 'sort':
        a_llist.sort()


    elif operation == 'maximum':
        a_llist.max()

    elif operation == 'minimum':
        a_llist.min()

    elif operation == 'sum':
        a_llist.sum()

    elif operation == 'avg':
        a_llist.avg()




    elif operation == 'quit':
        break
