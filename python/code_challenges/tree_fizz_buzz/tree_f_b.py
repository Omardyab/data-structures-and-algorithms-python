import copy
"""Queue
    Create a Queue class that has a front property. It creates an empty Queue when instantiated.
    This object should be aware of a default empty value assigned to front when the queue is created."""
class Nodeq:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    """ enqueue
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance."""
    def enqueue(self, value):
        node = Nodeq(value)
       # rear node would point to new node and rear would alos be new node
        if self.rear:
            self.rear.next = node
            self.rear = node
        # otherwise the node would be both rear and front
        else:
            self.rear=self.front = node
    """peek
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack"""
    def peek(self):
        # as peek is from front(head) then we check front first that its not empty
        if self.front == None:
            raise AttributeError("Your Queue is empty with value of None")
        # view the value of front (head) of our stack
        return self.front.value
    """is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty"""
    def isEmpty(self):
        # either ways are correct
        # first one
        if self.rear:
            return False
        return True
        # second method
        # return not self.rear
    """dequeue
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
    def dequeue(self):
        # move the front to the next value and remove the current one , but first if we have one value then it will be none
        if self.front == None:
            raise AttributeError("Your Queue is empty with value of None")
        else:
            deq_value=self.front.value
            # new front will be the next node
            self.front =self.front.next
            # if new front is none again rear should be None too
            if self.front==None:
                self.rear=None
            return deq_value
    def __str__(self):
        check=self.front
        queue_strrep=""
        if check:
            while(check):
                queue_strrep += f"[{ check.value }] <= "
                check = check.next
        queue_strrep += "None"
        return queue_strrep

class Node:
    def __init__( self, value ):
        self.value = value
        self.children = []

class k_tree:
    def __init__( self ):
        self.root = None

    def __str__( self ):
        if self.root:
            result = [self.root.value]
            for child in self.root.children:
                result += [child.value]
            result = str(result)
            return result

        else:
            raise Exception("K array tree is empty")


def k_tree_fizz_buzz( k_tree ):

    copied_ktree = copy.deepcopy(k_tree)
    root = copied_ktree.root
    queues = Queue()
    if not root :
        raise Exception("K array tree is empty")
    def fizz_buzz(node):
        if node % 15==0:
            return ('FizzBuzz')
        elif node % 3 == 0:
            return ('Fizz')
        elif node % 5 == 0:
            return ('Buzz')
        else:
            return str(node)
# check each child and call fizz buzz
    if root :
        queues.enqueue( root )
    while not queues.isEmpty():
        nodes = queues.dequeue()
        nodes.value = fizz_buzz(nodes.value)
        for child in nodes.children:
            queues.enqueue( child )
    return copied_ktree

if __name__ == "__main__":
    k_tree=k_tree()
    k_tree.root = Node(2)
    k_tree.root = Node(2)
    k_tree.root.children += [Node(7)]
    k_tree.root.children += [Node(5)]
    k_tree.root.children += [Node(2)]
    k_tree.root.children += [Node(6)]
    k_tree.root.children += [Node(9)]
    k_tree.root.children += [Node(5)]
    k_tree.root.children += [Node(11)]
    k_tree.root.children += [Node(15)]
    print(k_tree)
    copied_k_tree=k_tree_fizz_buzz(k_tree)
    print(copied_k_tree)
