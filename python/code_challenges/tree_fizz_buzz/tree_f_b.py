"""first => Node => Create a Node class that has properties for the value stored in the Node, and a pointer to the next node"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""Stack
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created."""

class Stack:
    def __init__(self,node=None):
        self.top = None

    """The class should contain the following methods:
        push
        Arguments: value
        adds a new node with that value to the top of the stack with an O(1) Time performance."""

    def push(self, value):
        # preparing my node to be top
        node = Node(value)
        # moving top to next
        if self.top:
            node.next = self.top
        # new node on top
        self.top = node
    """pop
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack"""
    def pop(self):
        # check if top is none then raise an error
        if self.top == None:
            raise AttributeError("Your Stack is empty with value of None")
        # store  top in a temp value
        tempvalue = self.top
        # reassign top to be next on ein the stack
        self.top = self.top.next

        tempvalue.next=None
        return tempvalue.value
    """peek
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack"""
    def peek(self):
        # check if top is none then raise an error
        if self.top == None:
            raise AttributeError("Your Stack is empty with value of None")
        # check what is the value of the top of the stack
        return self.top.value

    """is empty
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty."""
    def isEmpty(self):
        # check the value of top if no then return True meaning your stack is empty(not false)
        return not self.top

    def __str__(self):
        check=self.top
        stack_strrep=""
        if check:
            while(check):
                stack_strrep += f"[{ check.value }] | "
                check = check.next
        stack_strrep += "None"
        return (stack_strrep)
    # def __str__(self):
    #     stack_str = ""
    #     if self.top:
    #         current = self.top
    #         while(current):
    #             stack_str += f"{ current.value } | "
    #             current = current.next
    #     stack_str += "NULL"
    #     return (stack_str)


"""Queue
    Create a Queue class that has a front property. It creates an empty Queue when instantiated.
    This object should be aware of a default empty value assigned to front when the queue is created."""
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    """ enqueue
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance."""
    def enqueue(self, value):
        node = Node(value)
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



def fizz_buzz_tree(tree):
    if not tree.root:
        return tree
    if tree.root.value % 5 == 0 and tree.root.value % 3 == 0:
        tree.root.value = 'FizzBuzz'
    elif tree.root.value % 3 == 0:
        tree.root.value = "Fizz"
    elif tree.root.value % 5 == 0:
        tree.root.value = "Buzz"
    else:
        tree.root.value = str(tree.root.value)
    return tree.root.value
