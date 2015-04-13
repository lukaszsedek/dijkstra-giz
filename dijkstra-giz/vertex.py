
import sys

""" 
Lukasz Sedek
lukasz.sedek@pjwstk.edu.pl
License Apache Common 2.0

For Dijkstra algorithm we need only vertices with its adjacencies
flags:
  - visited - is visited by algorithm (loog avoidance, marking)
  - distance - metric used by Dijkstra for path choice
  - previous - just for sake of precedency
  - id - label of this vertex/node
"""
class Vertex:
  def __init__(self, node):
    self.id = node 
    self.adjacent = {} 
    # Set distance to infinity for all nodes 
    self.distance = sys.maxint
    # Mark all nodes unvisited
    self.visited = False 
    # Predecessor 
    self.previous = None


  # add new neigbor
  def add_neighbor(self, neighbor, weight=0):
    self.adjacent[neighbor] = weight

  # get connection
  def get_connections(self):
    return self.adjacent.keys()

  # getter for ID 
  def get_id(self): 
    return self.id
  

  # getter for weight
  def get_weight(self, neighbor):
    return self.adjacent[neighbor] 

  # setter for distance
  def set_distance(self, dist): 
    self.distance = dist 

  # getter for distance
  def get_distance(self):
    return self.distance 

  # setter for previous
  def set_previous(self, prev):
    self.previous = prev
  
  # marking as visited node
  def set_visited(self):
    self.visited = True 
 
  # overriden str() method
  def __str__(self):
    return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])