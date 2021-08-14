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



def linked_list_zip(f_list,s_list):
        if f_list.head is None and s_list.head is None:
            return None
        if f_list.head is None:
            return f_list
        if s_list.head is None:
            return s_list
        flist_current=f_list.head
        fnext=flist_current.next
        slist_current=s_list.head
        snext=slist_current.next
        while fnext and snext:
            flist_current.next=slist_current
            slist_current.next=fnext
            flist_current=fnext
            slist_current=snext
            fnext=fnext.next
            snext=snext.next
        if fnext is None and snext is None:
            flist_current.next=slist_current
        elif fnext is not None:
            flist_current.next=slist_current
            slist_current.next=fnext
        elif snext is not None:
            slist_current.next=slist_current
            flist_current.next=snext
        return str(f_list)


if __name__ == "__main__":
    ll1 =Linkedlist()
    ll1.insert(7)
    ll1.insert(5)
    ll1.insert(3)
    ll1.insert(1)
    print(ll1)
    ll2=Linkedlist()
    ll2.insert(8)
    ll2.insert(6)
    ll2.insert(4)
    ll2.insert(2)
    print(ll2)
    new=linked_list_zip(ll1,ll2)
    print(new)

