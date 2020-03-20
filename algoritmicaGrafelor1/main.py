from domain import Graph
from interface import userInterface


TheGraph=Graph("graph1k.txt")
UI=userInterface(TheGraph)
UI.run()