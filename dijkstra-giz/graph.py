
from vertex import Vertex
'''
Class which represents overall Graph
Lukasz Sedek
lukasz.sedek@pja.edu.pl
License Apache Common 2.0
'''
class Graph:
  def __init__(self):
    self.vert_dict = {}
    self.num_vertices = 0

  def __iter__(self):
    return iter(self.vert_dict.values())

  # add new vertex
  # construct graph only
  def add_vertex(self, node):
    self.num_vertices = self.num_vertices + 1
    new_vertex = Vertex(node)
    self.vert_dict[node] = new_vertex
    return new_vertex

  # get vertex
  def get_vertex(self, n):
    if n in self.vert_dict:
      return self.vert_dict[n]
    else: 
      return None

  # add edge between vertices
  def add_edge(self, frm, to, cost = 0):
    if frm not in self.vert_dict:
      self.add_vertex(frm)
    if to not in self.vert_dict:
      self.add_vertex(to) 

    self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

  # vertices getter
  def get_vertices(self):
    return self.vert_dict.keys()

  # set previous vertex
  def set_previous(self, current):
    self.previous = current

  # get previous vertex
  def get_previous(self, current):
     return self.previous

  # get size of the graph - vertex
  def get_vertex_number(self):
  	return len(self.vert_dict)


    
    
    
  	
  	
