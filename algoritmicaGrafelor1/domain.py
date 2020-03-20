from path import bfs,getPath,dijkstra
import rootedTree
class Graph:
    def __init__(self,fileName):
        self.dictIn={}
        self.dictOut={}
        self.dictCosts={}
        self.listOfEdges=[]
        self.fileName=fileName
        self.takefromFile()


    def parseX(self):
        """Returns an iterable containing all the vertices"""
        return self.dictOut.keys()

    def parseNout(self, x):
        """Returns an iterable containing the outbound neighbours of x"""
        return self.dictOut[x]

    def parseNin(self, x):
        """Returns an iterable containing the inbound neighbours of x"""
        return self.dictIn[x]

    def isEdge(self, x, y):
        """Returns True if there is an edge from x to y, False otherwise"""
        if y in self.parseX() or x  in  self.parseX():
            return y in self.dictOut[x]
        else :
            print("verteces not found")

    def addEdge(self, x, y,z):
        """Adds an edge from x to y.
        Precondition: there is no edge from x to y"""
        if self.isEdge(x,y)==False:
            self.dictOut[x].append(y)
            self.dictIn[y].append(x)
            self.listOfEdges.append((x, y))
            self.dictCosts[(x,y)]=z
        else:
            print("Allready is an edge between them!")

    def addVertex(self,x):
        """
        Add an vertex to te dictionary
        :param x: the vertex to be added
        :return: th dictionary has one more vertex
        """
        self.dictOut[x]=[]

    def removeEdge(self,vertexIn ,vertexOut):
        """Removes an edge from all the dictionaries"""

        if vertexOut in self.dictOut[vertexIn]:
             self.dictOut[vertexIn].remove(vertexOut)
        if vertexIn in self.dictIn[vertexOut]:
            self.dictIn[vertexOut].remove(vertexIn)
        if self.isEdge(vertexIn,vertexOut)==False:
            for index in range(0,len(self.listOfEdges)):
                if self.listOfEdges[index]==(vertexIn,vertexOut):
                    edge_id=index
            self.listOfEdges.remove((vertexIn,vertexOut))
            del self.dictCosts[(vertexIn,vertexOut)]
            return 1

    def removeVertex(self,x):
        """Removes a vertex from all the dictionaries"""
        if x in self.dictOut.keys():
            del self.dictOut[x]
        for y in self.dictIn.keys():
            if x in self.dictIn[y]:
                self.dictIn[y].remove(x)




    def modifyCost(self,firstV,secondV,costToBe):
        self.dictCosts[(firstV,secondV)]=costToBe

    def copyGraph(self):
        graphDict={}
        for i in range(len(self.listOfEdges)):
            graphDict[i]=[]
            graphDict[i].append(self.listOfEdges[i][0])
            graphDict[i].append(self.listOfEdges[i][1])
            graphDict[i].append(self.dictCosts[(self.listOfEdges[i][0],self.listOfEdges[i][1])])
            print(graphDict[i])




    def takefromFile(self):
        openFile=open(self.fileName,"r")
        line = openFile.readline().strip()
        line=line.split(" ")
        edges=int(line[1])

        for i in range (0,int(line[0])):
            self.dictIn[i]=[]
            self.dictOut[i]=[]

        line = openFile.readline().strip()
        line = line.split(' ')
        i=1

        while i<= edges:
            self.dictOut[int(line[0])].append(int(line[1]))
            self.dictIn[int(line[1])].append(int(line[0]))
            self.dictCosts[(int(line[0]),int(line[1]))]=int(line[2])
            self.listOfEdges.append((int(line[0]),int(line[1])))

            line = openFile.readline().strip()
            line = line.split(' ')
            i += 1
        openFile.close()

    def shortest_path_backward_bfs(self, first_vertex, second_vertex):

        b=[]
        a=bfs(self,first_vertex)
        b=getPath(a,second_vertex)

        return b[0], b[1]


    def getShortestCostWalk(self,first_vertex,second_vertex):
        cost=self.dictCosts
        tree = dijkstra(self, cost, first_vertex)
        #print (tree)
        print( getPath(tree,second_vertex))


