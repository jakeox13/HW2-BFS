import networkx as nx
from collections import deque
class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # Check to make sure inputs are valid

        # Check for empty graph
        if  len(list(self.graph.nodes))==0:
            raise ValueError("This graph is empty")
        # Check for vaild starting point
        if start not in list(self.graph.nodes):
            raise ValueError("Starting node is not present in graph")
        # Check for vaild end if one is given
        if end != None and end not in list(self.graph.nodes):
            raise ValueError("Ending node is not present in graph")
        
        # Intialize the queue object
        Q= deque()

        # Initilaize the list of nodes visited 
        visited=[start]
        
        # Add starting node to queue
        Q.append(start)
        
        end_found=False
        # Create a dictionary of paths taken to each node
        path= dict()
        # Add the start to the path of all others
        path[start]=[start]
        # Loop through node
        while Q and not end_found:
            # Get first value in queue
            v=Q.popleft()
            # get neighbors of node you are investigating
            n = self.graph.adj[v]

            # Check if each neighbor has been visted if visted pass
            for w in n:
                if w not in visited:
                    # If not visited add to queue and add to visted list
                    visited.append(w)
                    Q.append(w)
                    # Set the path of current to path of previous + current
                    if end != None:
                        path[w]=path[v]+[w]
                    # If this is end node stop searching
                    if w == end:
                        end_found= True


        if end == None:
            return visited
        elif end_found == False:
            return None
        else:
            return path[end]