
from vertex import Vertex

class Graph:
  # ctor
  def __init__(self, ):
    self.vertices_number = 0	# vertices number
    self.vert = {}				# vertices

  # to string str() override
  def __str__(self):
  	temp_str = ""
  	for v in self.vert:
  		temp_str.join(v)
  		temp_str.join("\n")
  	return temp_str