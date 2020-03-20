class RootedTree:

    def __init__(self, root):
        self.root = root
        self.children = {}
        self.children[self.root] = []
        self.parent = {}
        self.parent[self.root] = None

    def addChild(self, parent, child):
        '''
        Preconditions: parent - existing node of the tree
                child - is not an existing node
        '''
        self.children[parent].append(child)
        self.children[child] = []
        self.parent[child] = parent

    def reparent(self, parent, child):
        '''
            Adds or moves (re-parents) a child under the given parent
            Pre: Parent is an existing vertex
        '''
        if child in self.parent.keys():
            oldParent = self.parent[child]
            self.children[oldParent].remove(child)
        else:
            self.children[child] = []
        self.parent[child] = parent
        self.children[parent].append(child)

    def parseChildren(self, node):
        '''
        Preconditions: node - existing node of the tree
        '''
        return list(self.children[node])

    def getParent(self, node):
        '''
        return None for the root, the parent node otherwise
        precondition: the node must exist
        '''
        return self.parent[node]

    def subtreeToString(self, subtreeRoot, tabCount=0):
        string = "\t" * tabCount + str(subtreeRoot) + "\n"
        for child in self.parseChildren(subtreeRoot):
            string += self.subtreeToString(child, tabCount + 1)
        return string

    def __str__(self):
        return self.subtreeToString(self.root)

    def nodeExits(self, node):
        return node in self.parent.keys()
