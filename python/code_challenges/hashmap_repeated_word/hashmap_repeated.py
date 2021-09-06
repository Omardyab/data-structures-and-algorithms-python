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
import re
class HashTable :

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None]*size

    def hash(self, key):
        sum= 0
        for char in key:
            sum += ord(char)
        hashed_key  = (sum * 19) % self.size
        return hashed_key

    def add(self,key,value):
        idx = self.hash(key)
        if self._buckets[idx] == None:
            self._buckets[idx] = Linkedlist()
        self._buckets[idx].append([key,value])

    def get(self,key):
        idx = self.hash(key)
        if self._buckets[idx] == None:
            return None
        else:
            curr=self._buckets[idx].head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next

    def contains(self,key):
        idx=self.hash(key)
        if self._buckets[idx]:
            return self._buckets[idx].includes(key)
        else:
            return False


def if_word_repeated(word):
    hastable=HashTable()
    words=re.findall(r'\w+', word)
    if words == '':
        raise Exception("No word detected")
    for word in words:
        new_words = word.upper()
        if hastable.contains(new_words):
            return new_words
        else:
            hastable.add(new_words)

    return 'this is completely new'

if __name__=='__main__':

    print(if_word_repeated("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
