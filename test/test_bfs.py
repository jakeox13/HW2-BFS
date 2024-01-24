# write tests for bfs
import pytest
from search import Graph
import networkx as nx
from collections import deque



def test_bfs_traversal():
    """
    Unit tests for a breadth-first
    traversal using the 'tiny_network.adjlist'
    """
    # Read in graph
    test=Graph("data/tiny_network.adjlist")

    # Check to make sure the output is what is expected
    assert test.bfs('Michael Keiser') == ['Michael Keiser', '33232663', 'Charles Chiu', 'Martin Kampmann', '33242416', '33483487', '32790644', '31806696', '31626775', '31540829', 'Atul Butte', 'Luke Gilbert', 'Steven Altschuler', 'Lani Wu', 'Neil Risch', 'Nevan Krogan', '33765435', '31395880', '30944313', '32036252', '32042149', '30727954', '29700475', '34272374', '32353859', 'Marina Sirota', 'Hani Goodarzi', 'Michael McManus', '31486345', '32025019']
    assert test.bfs('Lani Wu') == ['Lani Wu', '32042149', '32036252', '31806696', '30727954', 'Hani Goodarzi', 'Steven Altschuler', 'Luke Gilbert', 'Michael McManus', '33232663', '33483487', '31626775', '31540829', '32025019', '29700475', 'Charles Chiu', 'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', 'Atul Butte', 'Michael Keiser', '33242416', '32790644', '34272374', '32353859', '30944313', '33765435', '31395880', 'Marina Sirota', '31486345']
    
    with pytest.raises(ValueError, match= r"Starting node is not present in graph"):
        test.bfs('Jake Oxendine')
    pass

def test_bfs():
    """
    Unit test fora breadth-first 
    using the 'citation_network.adjlist' 
    """
    test=Graph("data/citation_network.adjlist")
    # Test correct implimentation
    assert test.bfs("Michael Keiser","Atul Butte") == ['Michael Keiser', '33232663', 'Charles Chiu', '33242416', 'Atul Butte']
    
    # Test missing ending node implimentation
    with pytest.raises(ValueError, match= r"Ending node is not present in graph"):
        test.bfs('Marina Sirota','Jake Oxendine')

    # Test not connecting nodes return 1
    assert test.bfs('Marina Sirota','Alexander (Sandy) Johnson') == None

