class BinaryNode:
    """This implementation only saves the references to the children"""

    def __init__(self, elem: object,
                 left: "BinaryNode" = None,
                 right: "BinaryNode" = None) -> None:
        self.elem = elem
        self.left = left
        self.right = right

    def __eq__(self, other: 'BinaryNode') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and \
               self.left == other.left and self.right == other.right
class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def __eq__(self, other: 'BinaryTree') -> bool:
        """checks if two binary trees are equal o not"""
        return other is not None and self._root == other._root

    def size(self) -> int:
        """Returns the number of nodes"""
        return self._size(self._root)

    def _size(self, node: 'BinaryNode') -> int:
        """return the size of the subtree from node"""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: 'BinaryNode') -> int:
        """return the height of node"""
        if node is None:
            return -1

        return 1 + max(self._height(node.left), self._height(node.right))

    def preorder(self) -> None:
        """prints the preorder (root, left, right) traversal of the tree"""
        self._preorder(self._root)

    def _preorder(self, node: 'BinaryNode') -> None:
        """prints the preorder (root, left, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            print(node.elem)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self) -> None:
        """prints the postorder (left, right, root)  traversal of the tree"""
        self._postorder(self._root)

    def _postorder(self, node: 'BinaryNode') -> None:
        """prints the postorder (left, right, root) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem)

    def inorder(self) -> None:
        """prints the inorder (left, root, right)  traversal of the tree"""
        self._inorder(self._root)

    def _inorder(self, node: 'BinaryNode') -> None:
        """prints the inorder (left, root, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._inorder(node.left)
            print(node.elem)
            self._inorder(node.right)

    def level_order(self) -> None:
        """prints the level order of the tree.
        We will use an array (Python List) to save the
        nodes that you are visiting. Instead of using an array,
        you could use a Queue (import queue)"""
        if self._root is None:
            print('tree is empty')
        else:
            # we use a Python list to save the binary nodes
            q = [self._root]
            while not q.empty():
                current = q.pop(0)  # dequeue, get the first node
                print(current.elem)
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: 'BinaryNode',is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)
class BinarySearchTree(BinaryTree):

    def search(self, elem: object) -> BinaryNode:
        """Returns the node whose elem is elem"""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode:
        """Recursive function"""
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)

    def searchit(self, elem: object) -> BinaryNode:
        """iterative function"""
        node = self._root
        while node:
            if node.elem == elem:
                # we have found it!!! we can return it and leave the function
                return node

            if elem < node.elem:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def insert_iterative(self, elem: object) -> None:
        """iterative version of insert"""
        if self._root is None:
            self._root = BinaryNode(elem)  # if tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                node = node.left
                if node.left is None: # this is the place to insert it
                    node.left = BinaryNode(elem)
                    not_exist = False

            elif elem > node.elem:
                node = node.right
                if node.right is None:  # this is the place to insert it
                    node.right = BinaryNode(elem)
                    not_exist = False

            else:  # elem == node.elem
                print('duplicate elements not allowed!!')
                not_exist = False

    def _minimum_node(self, node: BinaryNode) -> BinaryNode:
        """returns the  node with the smallest elem
        in the subtree node.
        This is the node that is furthest to the left"""
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """It recursively searches the node. When the node is
        found, the node has to be removed"""
        if node is None:
            print(elem, ' not found')
            return node

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                return None

            # Case 2: node only has a child, so the function has to return it
            if node.left is None:
                # It only has the right child
                return node.right

            elif node.right is None:
                # It only has the left child
                return node.left
            else:
                # Case 3: node.left!=None and node.right!=None
                # we search the smallest node from its right child
                successor = self._minimum_node(node.right)
                # we replace elem with the elem of the successor
                node.elem = successor.elem
                # now, we have to remove successor from the right child
                node.right = self._remove(node.right, successor.elem)

        return node


        
    
    
        


tree=AVLTree()
for i in [3,2,1]:
    tree.insert(i) 
tree.draw()

tree.equilibrar()
tree.draw()
