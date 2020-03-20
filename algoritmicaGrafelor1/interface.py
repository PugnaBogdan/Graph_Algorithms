from domain import Graph

class userInterface:
    def __init__(self,graph):
        self._graph=graph

    def _uiAddEdge(self,parameters):
        parameters[0]=int(parameters[0])
        parameters[1]=int(parameters[1])
        parameters[2]=int(parameters[2])
        if parameters[0]>1000 or parameters[1]>1000or parameters[0] not in self._graph.parseX()or parameters[1] not in self._graph.parseX() :
            print("There are no vertexes that large")
        else:
            self._graph.addEdge(parameters[0],parameters[1],parameters[2])

    def _uiGetVertices(self,parameters):
        setOfver=[]
        for i in  self._graph.parseX():
            setOfver.append(i)
        print(setOfver)

    def _uiGetNumberOfVerices(self,parameters):
        setOfver=self._graph.parseX()
        k=0
        for i in setOfver:
            k+=1
        print (k)

    def _uiIsAnEdge(self,parameters):
        parameters[0]=int(parameters[0])
        parameters[1] = int(parameters[1])

        print(self._graph.isEdge(parameters[0],parameters[1]))

    def _uiIndegree(self,parameters):
        parameters=int(parameters[0])
        i=0
        if parameters not in self._graph.parseX():
            print("The vertex doesn't exist anymore")
        else:
            for d in self._graph.parseNin(parameters):
                i+=1
            print(i)


    def _uiOutDegree(self,parameters):
        parameters=int(parameters[0])
        i = 0
        if parameters not in self._graph.parseX():
            print("The vertex doesn't exist anymore")
        else:
            for d in self._graph.parseNout(parameters):
                i += 1
            print(i)

    def _uiOutboundEdges(self,parameters):
        parameters=int(parameters[0])
        if parameters not in self._graph.parseX():
            print("The vertex doesn't exist anymore")
        else:
            print(self._graph.parseNout(parameters))

    def _uiINboundEdges(self,parameters):
        parameters=int(parameters[0])
        if parameters not in self._graph.parseX():
            print("The vertex doesn't exist anymore")
        else:
            print(self._graph.parseNin(parameters))

    def _uiAddVertex(self,parameters):
        parameters=int(parameters[0])
        if parameters  in self._graph.parseX():
            print("The vertex allready exists")
        else:
            self._graph.addVertex(parameters)

    def _uiRemoveEdge(self,parameters):
        parameters[0]=int(parameters[0])
        parameters[1] = int(parameters[1])
        if parameters[0] not in self._graph.parseX()or parameters[1] not in self._graph.parseX():
            print("the verteces doesn't exist!")
        else:
            self._graph.removeEdge(parameters[0],parameters[1])
    def _uigetShortestPath(self,parameters):
        parameters[0] = int(parameters[0])
        parameters[1] = int(parameters[1])
        if parameters[0] not in self._graph.parseX() or parameters[1] not in self._graph.parseX():
            print("the verteces doesn't exist!")
        else:
            c=self._graph.shortest_path_backward_bfs(parameters[1],parameters[0])
            if c[1]!=0 and c[1]!=1:
                print("path: "+str(c[0]),"lenght: "+str(c[1]))
            else:
                print("There is no path")


    def _uiRemoveVertex(self,parameters):
        parameters=int(parameters[0])
        if parameters not in self._graph.parseX():
            print("The vertex doens't exist")
        else:
            self._graph.removeVertex(parameters)

    def _uiCopyGraph(self,parameters):
        self._graph.copyGraph()

    def _uiModifyIntegerOfAnEdge(self,parameters):
        edgeId=int(parameters[0])
        intToBeModified=int(parameters[1])
        self._graph.modifyCost(edgeId,intToBeModified)

    def printListOfEdges(self,parameters):
        for i in range(0,len(self._graph.listOfEdges)):
            print(self._graph.listOfEdges[i])

    def _uiGetTheEndPointsOfAnEdge(self,parameters):
        edgeId=int(parameters[0])
        for i in range(0,len(self._graph.listOfEdges)):
            if i ==edgeId:
                print(self._graph.listOfEdges[i])

    def _uigetLowestCostWalk(self,parameters):
        self._graph.getShortestCostWalk(int(parameters[0]),int(parameters[1]))
    def _uiMenu(self):
        print("This is a program that models a graph.\n"
              "Get number of vertices : 1\n"
              "Desplay all vertices by pressing : 2\n"
              "Given two vertices, find out whether there is an edge from the first one to the second one : 3\n"
              "Parse (iterate) the set of outbound edges of a specified vertex : 4\n"
              "Parse the set of inbound edges of a specified vertex : 5\n"
              "Get the endpoints of an edge specified by an Edge_id (if applicable) : 6\n"
              "Retrieve or modify the information (the integer) attached to a specified edge : 7\n"
              "Add vertex by pressing : 8\n"
              "Remove Vertex : 9\n"
              "Add edge by pressing : 10\n"
              "Remove edge : 11\n"
              "Copy of the Graph : 12\n"
              "In degree : 13\n"
              "Out degree : 14\n"
              "Shortest path: 15\n"


              )


    def run(self):
        self._uiMenu()
        commands={
            "1":self._uiGetNumberOfVerices,
            "10":self._uiAddEdge,
            "2":self._uiGetVertices,
            "3":self._uiIsAnEdge,
            "11": self._uiRemoveEdge,
            "4":self._uiOutboundEdges,
            "5": self._uiINboundEdges,
            "6":self._uiGetTheEndPointsOfAnEdge,
            "7":self._uiModifyIntegerOfAnEdge,
            "8":self._uiAddVertex,
            "9":self._uiRemoveVertex,
            "12":self._uiCopyGraph,
            "13":self._uiIndegree,
            "14":self._uiOutDegree,
            "200":self.printListOfEdges,
            "15":self._uigetShortestPath,
            "16":self._uigetLowestCostWalk

        }
        while True:
            cmd=input(">>")
            parameters=cmd.split(" ")
            if cmd=="exit":
                return
            if parameters[0] in commands:
                try:
                    commands[parameters[0]](parameters[1:])
                except ValueError as ve:
                    print("Invalid value!")
            else:
                print("Invalid command!")

