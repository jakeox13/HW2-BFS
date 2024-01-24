import networkx as nx
import warnings
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
        The goal of this function is to traverse a graph in a breadth first manner. It will either traverse all nodes or find the shortest path between two nodes

        Args:
            start (string): The label on the node to start traversal or shortest path search
            end (string, optional): The label on the ending node for path first  Defaults to None.

        Raises:
            ValueError: If graph is empty
            ValueError: If starting node given is not in graph
            ValueError: If the ending node given is not in graph

        Returns:
            list: If only starting node , returns all nodes connected in order of traversal. if end is given it is shortest path between nodes, ifn not connected , returns None
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
        
        # Initlize search sucess
        end_found=False

        # This sets up my path recording
        # Create a dictionary of paths taken to each node
        path= dict()
        # Add the start to the path of all others
        path[start]=[start]

        # Loop through nodes and then neighbors until all avaiable nodes traversed or end of search found
        while Q and not end_found:
            
            # Get first value in queue
            v=Q.popleft()
            # get neighbors of node you are investigating
            n = self.graph.adj[v]

            # Check if each neighbor has been visted and if visted pass
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

        # If no end node was given return all traverse nodes
        if end == None:
            # Warn user if not all graph is visited
            if len(list(set(self.graph.nodes)-set(visited))):
                warnings.warn("Warning, not all nodes traversed")
            return visited
        
        # If ending node was vaild but not found
        elif end_found == False:
            return None
        
        # Will trigger if end was found and returns the path taken to the node
        else:
            return path[end]