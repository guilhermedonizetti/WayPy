"""
This example shows how to use the package to find the path from a starting point
to another point X.
And at the end, it finds the path from point X to an end point.
"""

#Import (import should always look like this)
from waypy.agent import Agente

#Instantiate the class
agent = Agente()

#Enter the values ​​of your problem:
agent.starting_points = ["D"] #list of valid starting points
agent.arrival_points = ["G"] #list of valid arrival points
agent.nodes = ["A", "B", "C", "D", "E", "F", "G"] #All points (nodes) of your graph
#list of adjacencies with connections between graph points
agent.graphs = [
    ["B", "D", "F"],
    ["A", "C", "G", "E"],
    ["B", "F", "G"],
    ["A", "F", "G"],
    ["B"],
    ["A", "C", "D"],
    ["B", "C", "D"]
]


#We can already try to find ways...
#To find a path using the method Profundidade Limitada:
#1) The first parameter "E" is where we want to go out of start_points.
#2) The second parameter is the method we want to use to fetch the path.
#3) The third parameter is the maximum allowable depth.
way = agent.encontrar_ajuda_humanitaria("E", "PROFUNDIDADE LIMITADA", 4)
print("Profundidade limitada: {}".format(way))

#To find a path using any method other than Profundidade Limitada:
#1) The first parameter "E" is where we want to go out of start_points.
#2) The second parameter is the method we want to use to fetch the path.
#Any method other than PRO does not take a third parameter.
way = agent.encontrar_ajuda_humanitaria("E", "AMPLITUDE")
print("Amplitude: {}".format(way))


#To find a way out:
#1) Inform the point that should start the search for the exit.
#2) Inform search method
way = agent.encontrar_atendimento("E", "AMPLITUDE")
print("Amplitude: {}".format(way))