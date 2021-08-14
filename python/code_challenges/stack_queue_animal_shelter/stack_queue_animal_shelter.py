class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""Stack
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created."""


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
            self.rear.next = self.rear=  node
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
class Dog:
    def __init__(self, name):
        self.name=name
        self.kind='dog'
        self.next=None
class Cat:
    def __init__(self, name):
        self.name=name
        self.kind='cat'
        self.next=None

class AnimalShelter():

    def __init__(self):
        self.front=None
        self.rear = None

    def enqueue(self, d):
        node = d
       # rear node would point to new node and rear would also be new node
        if self.rear:
            self.rear.next = self.rear=  node
        # otherwise the node would be both rear and front
        else:
            self.rear=self.front = node
            return f"your animal is now added to the shelter"


    def dequeue(self,pref=None):

            if pref is None:
                return f"you did not choose your animal"
            if self.front is None and not self.rear:
                raise Exception("Your shelter is empty")
            if self.front.kind == pref:
                curr = self.front
                self.front = self.front.next
                return curr.name
            else:
                curr = self.front
                while curr:
                    if curr.next.kind == pref:
                        current_node = curr.next.name
                        curr.next = curr.next.next
                        return current_node
                    else:
                        curr = curr.next

    def __str__(self):
        check=self.front
        queue_strrep=""
        if check:
            while(check):
                queue_strrep += f"[{ check.name }] <= "
                check = check.next
        queue_strrep += "None"
        return (queue_strrep)


if __name__ == "__main__":

    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat('Lucy'))
    animal_queue.enqueue(Dog('Husky'))
    animal_queue.enqueue(Dog('Tiger'))
    animal_queue.enqueue(Cat('Kitty'))

    print(animal_queue)
    animal_queue.dequeue('dog')
    print(animal_queue)
    animal_queue.dequeue('cat')
    print(animal_queue)
    animal_queue.dequeue()
    print(animal_queue)
    animal_queue.dequeue('cat')
    print(animal_queue)
