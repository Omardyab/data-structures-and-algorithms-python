
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



def breadth_first(t):
    l = []
    q = Queue()
    if not t.root:
        raise Exception("your tree is empty")
    q.enqueue(t.root)
    while not q.isEmpty():
        i = q.dequeue()
        l.append(i.value)
        if i.left if hasattr(i, 'left') else None:
            q.enqueue(i.left)
        if i.right if hasattr(i, 'right') else None:
            q.enqueue(i.right)
    return l
class Node:
    def __init__(self, value):
        self.value = value
        self.child = []

class Tree:
    def __init__(self, root=None):
        self.root = root

def fizz_buzz_tree(t):
    n_tree = t
    if not t.root:
        return t
    if n_tree.root.value % 15==0:
        n_tree.root.value = 'FizzBuzz'
    elif n_tree.root.value % 5 == 0:
        n_tree.root.value = "Buzz"
    elif n_tree.root.value % 3 == 0:
        n_tree.root.value = "Fizz"
    else:
        # convert the node value to string
        n_tree.root.value = str(n_tree.root.value)
    def rec_func(node):
        if node.child:
            # print("is working")
            for i in range(len(node.child)):
                rec_func(node.child[i])
                if node.child[i].value % 15==0:
                    node.child[i].value = 'FizzBuzz'
                elif node.child[i].value % 3 == 0:
                    node.child[i].value = "Fizz"
                elif node.child[i].value % 5 == 0:
                    node.child[i].value = "Buzz"
                else:
                    # convert the node value to string
                    node.child[i].value = str(node.child[i].value)
    rec_func(n_tree.root)
    
    return n_tree


if __name__ == "__main__":
    node = Node(5)
    node.child += [Node(15)]
    node.child += [Node(40)]
    node.child[0].child += [Node(30)]
    node.child[0].child += [Node(60)]
    node.child[1].child += [Node(5)]
    node.child[1].child += [Node(5)]
    node.child[0].child[1].child += [Node(6)]
    node.child[0].child[1].child += [Node(10)]
    node.child[0].child[1].child += [Node(18)]
    node.child[0].child[1].child += [Node(15)]
    node.child[1].child[1].child += [Node(30)]
    t = Tree(node)
    fizzy=fizz_buzz_tree(t)
    print(breadth_first(fizzy))








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

