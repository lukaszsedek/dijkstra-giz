
from vertex import Vertex
from graphviz import Digraph
'''
'''
class Graph:
  def __init__(self):
    self.vert_dict = {}
    self.num_vertices = 0
    self.dot = Digraph(comment='dijkstra-giz')
    self.dot.attr('node', shape='circle')
    self.dot.body.append(r'label = "\n\nDijkstra-GIZ\nLukasz Sedek"')
    self.dot.body.append('fontsize=20')
	
  def __iter__(self):
    return iter(self.vert_dict.values())

  def add_vertex(self, node):
    self.num_vertices = self.num_vertices + 1
    new_vertex = Vertex(node)
    self.vert_dict[node] = new_vertex
    self.dot.node(str(node), str(node))
    return new_vertex

  def get_vertex(self, n):
    if n in self.vert_dict:
      return self.vert_dict[n]
    else: 
      return None

  def add_edge(self, frm, to, cost = 0):
    if frm not in self.vert_dict:
      self.add_vertex(frm)
    if to not in self.vert_dict:
      self.add_vertex(to) 

    self.dot.edge(str(frm), str(to), label=str(cost))
    self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
    #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost) 

  def get_vertices(self):
    return self.vert_dict.keys()

  def set_previous(self, current):
    self.previous = current

  def get_previous(self, current):
     return self.previous

  def print_graph(self):
    print 'Graph data:' 
    for v in self: 
    	for w in v.get_connections():
  	    	vid = v.get_id()
  	    	wid = w.get_id()
  	    	print '( %s , %s, %3d)' % ( vid, wid, v.get_weight(w))

  def print_graphviz(self):
  	print(self.dot.source)
  	self.dot.render('img/image')

