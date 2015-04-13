
from vertex import Vertex
from graphviz import Digraph
import logging
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

  # print graphviz structure and save as graph.pdf
  # additional feature
  def print_graph(self, path_in):
    dot = Digraph(comment='Dijkstra-GIZ')
    dot.body.append(r'label = "\n\nDijkstra-GIZ\nLukasz Sedek"')
    dot.body.append('fontsize=20')
    dot.attr('node', shape='circle')
    # iterate all vertices and its edges
    for v in self:
    	if v.get_id() in path_in:
    		dot.node(str(v.get_id()), str(v.get_id()) + "(" + str(v.get_distance()) + ")", color="RED")
    	else:
    		dot.node(str(v.get_id()), str(v.get_id()) + "(" + str(v.get_distance()) + ")" )
    	for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            if ((vid in path_in) and (wid in path_in) ):
            	dot.edge(str(vid), str(wid), label=str(v.get_weight(w)), color="RED")
            else:
            	dot.edge(str(vid), str(wid), label=str(v.get_weight(w)))
            logging.debug('( %s , %s, %3d)' % ( vid, wid, v.get_weight(w)))
    dot.render('graph')
    logging.debug(dot.source)
    

    
    
    
  	
  	
