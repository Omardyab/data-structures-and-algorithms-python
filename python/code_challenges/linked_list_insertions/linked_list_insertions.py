class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    """
    define insert method which adds value in head
    """
    def insert(self, value='null'):
        try:
            first_node = Node(value)
            if not self.head:
                self.head = first_node
            else:
                current_node = self.head
                self.head=first_node
                self.head.next = current_node
        except Exception as exception:
            raise Exception(f"its not working as it should be: {exception}")
    """
    define include method which check if value exisited (in this case return false) otherwise return True
    """
    def includes(self, expectedvalue):
        try:
            current_node = self.head
            while current_node:
                if current_node.value == expectedvalue:
                    return True
                    break
                current_node = current_node.next
            return False
        except Exception as exception:
                raise Exception(f"its not working as it should be: {exception}")
    """
    Visual representation of the linked list bubbles
    """
    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            value = current_node.value
            if current_node.next is None:
                result =result+ f"({value})-> None"
                break
            result = result + f"({value}) -> "
            current_node=current_node.next
        return result

    """
    define append method which adds value to the end of the list
    head -> [1] -> [3] -> [2] -> X 	(5_	head -> [1] -> [3] -> [2] -> [5] -> X
    """
    def append(self,value="None"):
        new_node = Node(value)
        if self.head==None:
            self.head=new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        #     while current_node !=None:
        #         print(current_node.value)
        #         print("looping")
        #         current_node=current_node.next
        # if current_node ==None:
        #     print("its none")
        #     current_node=self.value
        #     current_node.next=None
    """
    define inset_before method which adds value before specific node
    head -> [1] -> [3] -> [2] -> X	(3, 5)	head -> [1] -> [5] -> [3] -> [2] -> X
    """
    def insert_before(self,first,second):
        head_node=self.head
        current_node=Node(second)
        if head_node.value==first:
             current_node.next = self.head
             self.head = head_node
        else:
            while head_node:
                if head_node.next.value==first:
                    current_node.next=head_node.next
                    head_node.next=current_node
                    break
                head_node=head_node.next
    def insert_after(self,first,second):
        head_node=self.head
        new_node=Node(second)
        while head_node:
            if head_node.value==first:
                next_head=head_node.next
                head_node.next=new_node
                head_node.next.next=next_head
                break
            head_node=head_node.next



if __name__ == "__main__":

    myll=Linkedlist()
    print("my linked list now have : ",myll)
    myll.insert(1)
    print("my linked list now have : ",myll)
    myll.insert(2)
    print("my linked list now have : ",myll)
    myll.insert(7)
    print("my linked list now have : ",myll)
    myll.includes(7)
    print("my linked list now have : ",myll)
    myll.includes(9)
    print("my linked list now have : ",myll)
    print(myll)
    myll.append(8)
    print(myll)
    myll.insert_before(2,1)
    print(myll)
    myll.insert_before(7,8)
    print(myll)
    myll.insert_before(1,5)
    print(myll)
    myll.insert_after(7,3)
    print(myll)
    myll.insert_after(3,4)
    print(myll)
