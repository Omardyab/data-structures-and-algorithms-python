class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        l = []
        def p_order(root):
            l.append(root.value)
            if root.left:
                p_order(root.left)
            if root.right:
                p_order(root.right)
        p_order(self.root)
        return l

    def post_order(self):
        l=[]
        def po_order(root):
            if root.left :
                po_order(root.left)
            if root.right :
                po_order(root.right)
            l.append(root.value)
        po_order(self.root)
        return l

    def in_order(self):
        l=[]
        def inorder(root):
            if root.left :
                inorder(root.left)
            l.append(root.value)
            if root.right :
                inorder(root.right)
        inorder(self.root)
        return l

class Binary_Search_Tree(BinaryTree):
    def __init__(self,root=None):
        self.root=root

    def add(self,val):

        if self.root is None:
            self.root=Node(val)
        curr_root=self.root
        while curr_root !=None:
            if curr_root.value>val:
                if curr_root.left is None:
                    curr_root.left=Node(val)
                else:
                    curr_root=curr_root.left

            elif curr_root.value<val:
                if curr_root.right is None:
                    curr_root.right=Node(val)
                else:
                    curr_root=curr_root.right
            if curr_root.value==val:
                return "this value is already exisited "

    def contains(self,value):

        if self.root is None:
            return False
        curr_root =self.root
        while curr_root:
            if curr_root.value==value:
                return True
            if value>curr_root.value:
                curr_root=curr_root.right
            else:
                curr_root=curr_root.left
        return False

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

# def breadth_first(self):
#     curr=self.root
#     q=Queue()
#     Queue.enqueue(curr)
#     l=[]
#     if curr== None:
#         raise Exception("Empty Tree")
#     # when there is no root
#     while curr:
#         curr=Queue.dequeue
#         l.append(curr.value)
#         if curr.left:
#             Queue.enqueue(curr.left)
#         if curr.right:
#             Queue.enqueue(curr.right)
#         if Queue.isEmpty:
#             raise Exception("No more roots")
#         return l
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

if __name__=="__main__":
    """ as taken from TA ahmad since no insert method yet"""
    bt = Binary_Search_Tree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    print(bt.pre_order())
    print(bt.in_order())
    print(bt.post_order())
    # B_s_tree = Binary_Search_Tree()
    # B_s_tree.add(59)
    # B_s_tree.add(40)
    # B_s_tree.add(98)
    # B_s_tree.add(100)
    # B_s_tree.add(4)
    # B_s_tree.add(56)
    # B_s_tree.add(6)
    # print("doe it contain 13 ? ",B_s_tree.contains(13))
    # print("doe it contain 4 ? ",B_s_tree.contains(4))
    # print("in pre order",B_s_tree.pre_order())
    # print("in order",B_s_tree.in_order())
    # print("in post order",B_s_tree.post_order())
    # print("doe it contain 56 ? ",B_s_tree.contains(56))
    # print("doe it contain 0 ? ",B_s_tree.contains(0))
    # bt=BinaryTree()
    # print(bt.max())
    print("Breadth first tree",breadth_first(bt))
