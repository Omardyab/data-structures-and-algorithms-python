
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
        if not self.top :
            raise Exception("Your Stack is empty with value of None")
        # store  top in a temp value
        tempvalue = self.top
        # # reassign top to be next on ein the stack
        self.top = self.top.next
        tempvalue.next=None
        return tempvalue.value
    """peek
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack"""
    def peek(self):
        # # check if top is none then raise an error
        # if self.top == None:
        #     raise AttributeError("Your Stack is empty with value of None")
        # check what is the value of the top of the stack
        return self.top.value

    """is empty
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty."""
    def isEmpty(self):
        # check the value of top if no then return True meaning your stack is empty(not false)
        return not self.top



class Pseudo_Queue:
    def __init__(self):
        self.base_stack = Stack() # pushing
        self.second_stack = Stack() # popping

    def enqueue(self, value):
        self.base_stack.push(value)

    def dequeue(self):
        if self.second_stack.top is None:
            if self.base_stack.top is None:
                raise Exception("empty queue dequeuing ")

            while self.base_stack.top:
                b_top = self.base_stack.pop()
                self.second_stack.push(b_top)

            dequeued_s = self.second_stack.pop()

            while self.second_stack.top:
                s_top = self.second_stack.pop()
                self.base_stack.push(s_top)
            return dequeued_s

    def __str__(self):
        check=self.base_stack.top
        stack_strrep=""
        if check:
            while(check):
                stack_strrep += f"[{ check.value }] | "
                check = check.next
        stack_strrep += "None"
        return (stack_strrep)

if __name__ == "__main__":

    q1=Pseudo_Queue()
    q1.enqueue(1)
    q1.peek()
    print(q1.value)


