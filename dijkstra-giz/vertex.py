
import sys

""" TODO OPIS
"""
class Vertex:
  def __init__(self, label):
    self.label = label
    self.is_visited = False
    self.distance = sys.maxint # MAX int as infinity 
    self.previous = None

  def __str__(self):
  	return str(self.label)
