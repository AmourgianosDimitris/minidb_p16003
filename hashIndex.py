'''
https://en.wikipedia.org/wiki/Hash_table
'''

class HashNode:
    '''
    Node abstraction. Represents a single bucket
    '''

    def __init__(self, values, child=None, next=None, parent=None):
        self.values = values
        self.child = child
        self.next = next
        self.parent = parent

    '''
        Insert the value and its ptr/s to the appropriate place (node wise).
        User can input two ptrs to insert to a non leaf node.

        value: the value that we are inserting to the node
        ptr: the ptr of the inserted value (its index for example)
        ptr1: the 2nd ptr (in case the user wants to insert into a nonleaf node for ex)
    '''

class HashIndex:
    def __init__(self, b, column_id):
        '''
        The Hash Index abstraction
        '''
        self.b = b # branching factor
        self.hashed_column = column_id
        self.nodes = None # list of nodes. Every new node is appended here
        self.head = None # the index of the root node

    def insert(self,column, values):
        # print (values)
        if column is not None:
            NewNode = HashNode(custom_hash_function(column))
            if self.head is None:
                self.head = NewNode
                tmp = HashNode(values)
                self.head.child = tmp
                tmp.parent = self.head
                return

            hash_prefix = self.head
            while hash_prefix:

                sum = 0
                if str(hash_prefix.values) == str(NewNode.values):
                    # print("hash: ", hash_prefix.values)
                    first_child = hash_prefix.child
                    next_child = hash_prefix.child
                    while next_child:

                        if next_child.child:
                            next_child = next_child.child
                        else:
                            break
                    tmp = HashNode(values)
                    next_child.child = tmp
                    tmp.parent = next_child
                    # print("bucket: ", next_child.child.values)
                    return
                if hash_prefix.next:
                    hash_prefix = hash_prefix.next
                else:
                    break
            hash_prefix.next=NewNode
            tmp = HashNode(values)
            hash_prefix.next.child = tmp
            tmp.parent = hash_prefix.next

    def split_to_buckets(self):
        b = self.b
        c_id = self.hashed_column

        hash_prefix = self.head

        sum = 0
        while hash_prefix is not None:
            sum = 0

            first_child = hash_prefix.child
            next_child = hash_prefix.child
            while next_child:
                sum += 1
                if sum>b:

                    parent = next_child.parent
                    first_child.next = next_child
                    first_child = next_child
                    parent.child = None
                    sum = 0

                if next_child.child:
                    next_child = next_child.child
                else:
                    sum = 0
                    break

            hash_prefix = hash_prefix.next

    def show(self):
        print ("\nPrint from show function")

        tmp = self.head
        while tmp is not None:

            print ('\nkey :', tmp.values)
            bucket = tmp.child
            while bucket is not None:
                tmp_child = bucket.child
                print ('  bucket: ')
                print ("  ->", bucket.values)
                while tmp_child is not None:
                    print ("  ->", tmp_child.values)
                    if tmp_child.parent:
                        tmp_child = tmp_child.child
                bucket = bucket.next
            tmp = tmp.next

    def hash_search(self, key):

        tmp = self.head
        c_id = self.hashed_column
        key_hash = custom_hash_function(key)
        while tmp:
            if str(tmp.values) == str(key_hash):

                bucket = tmp.child
                while bucket is not None:
                    if bucket.values[c_id] == key:
                        print ("->", bucket.values)

                    tmp_child = bucket.child
                    while tmp_child is not None:
                        if tmp_child.values[c_id] == key:
                            print ("->", tmp_child.values)
                        tmp_child = tmp_child.child

                    bucket = bucket.next
            tmp = tmp.next

    def hash_join_search(self, key, values):

        tmp = self.head
        c_id = self.hashed_column
        key_hash = custom_hash_function(key)
        while tmp:
            if str(tmp.values) == str(key_hash):

                bucket = tmp.child
                while bucket is not None:
                    if bucket.values[c_id] == key:
                        print ("\n->", bucket.values)
                        print (',', values)

                    tmp_child = bucket.child
                    while tmp_child is not None:
                        if tmp_child.values[c_id] == key:
                            print ("\n->", tmp_child.values)
                            print (',', values)
                        tmp_child = tmp_child.child

                    bucket = bucket.next
            tmp = tmp.next

def hash_function(column):
    sum = 0
    column_len = len(column)

    for val in [ord(c) for c in column]:
        sum = sum + val

    hash = sum % 2
    hash = hash ** column_len

    return hash

def custom_hash_function(column):
    sum = 0
    column_len = len(column)

    for val in [ord(c) for c in column]:
        sum = sum + val

    hash = sum % column_len
    hash = hash ** column_len

    return hash
