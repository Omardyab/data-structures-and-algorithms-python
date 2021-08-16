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
    def max(self):
        if self.root is None:
            return None
        max_value = self.root.value
        tree_nodes = self.in_order()

        for i in tree_nodes:
            if i > max_value:
                max_value = i
        return max_value

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
    # def max_bst(self):
    #     main_root = self.root
    #     while True:
    #         if main_root.right:
    #             main_root = main_root.right
    #         else:
    #             return main_root.value

if __name__=="__main__":
    """ as taken from TA ahmad since no insert method yet"""
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    # print(bt.pre_order())
    # print(bt.in_order())
    # print(bt.post_order())
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
    print(bt.max())
