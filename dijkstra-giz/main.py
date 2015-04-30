
#!/usr/bin/python
"""
Lukasz Sedek
Polsko-Japonska Akademia Technik Komputerowych
lukasz.sedek(at)pja.edu.pl 
License Apache 2.0
"""
from optparse import OptionParser
import logging, sys, heapq
from vertex import Vertex
from graph import Graph
from datetime import datetime

# global variables 
filename         = ""
edges_number     = 0


'''
Dijkstra algorithm which comuputes shortest path between two vertices.
Used python heapq implementation of priority heap
'''
def dijkstra(aGraph, start, target): 
  # Set the distance for the start node to zero 
  start.set_distance(0) 
  # 2. All other vertices are infinity (done by default on vertex)
  # Put all vertices in priority queue
  priority_queue = [(v.get_distance(),v) for v in aGraph] 
  heapq.heapify(priority_queue) 

  # 3. While heap is not empty...
  while len(priority_queue): 
    # pop vertex with lowest metric from queue
    uv = heapq.heappop(priority_queue)
    current = uv[1] 
    current.set_visited() 
 
    # 4 For all edges in given vertex
    for next in current.adjacent:
       # ...just loop avoidance :)
      if next.visited: 
   	    continue
   	  # update distance with calculated distance
      new_dist = current.get_distance() + current.get_weight(next)
      # but if distance is lower than previous
      # make it current distance. It's better metric
      if new_dist < next.get_distance():
      	next.set_distance(new_dist)
      	next.set_previous(current)
      	logging.debug("updated current: %s, next = %s, new_dist = %s",
      		current.get_id(), next.get_id(), next.get_distance())
      else:
      	# But if it's not, just skip this point
        logging.debug("not updated current: %s, next: %s new_dist = %s ",
         current.get_id(), next.get_id(), next.get_distance())

    # 5. last pop all from queue
    while len(priority_queue):
    	heapq.heappop(priority_queue)
    priority_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
    heapq.heapify(priority_queue)

# build array of vertices based on v.previous from target
def shortest(target, path):
  # recurrence
  if target.previous:
    path.append(target.previous.get_id())
    shortest(target.previous, path)
  return

# Parsing 1st line of config-topology file
# initialize both variables. In case of cast Error, exit
def parse_first_line_config( line ):
  try:
    vertex_number = int(line[0])
    logging.info("Vertex number: %s", vertex_number)
    for i in range(1, vertex_number+1):
      g.add_vertex(i)
    edges_number  = int(line[1])
  except ValueError:
    logging.error("CASE ERROR: COULD NOT PARSE 1ST LINE AS A NUMBER!!\n %s"
    	, line)
    sys.exit(0)

# Parsing other lines of config-topology file
# initialize 3 tuples. In case of cast Error, exit
def parse_edges(line):
  line_splited = line.split()
  frm = 0
  to = 0
  cost = 0
  try:
    frm    = int(line_splited[0])
    to     = int(line_splited[1])
    cost   = int(line_splited[2])
    logging.debug("Adding edge(%s, %s, %s)", frm, to, cost)
    g.add_edge(frm, to, cost)
  except ValueError:
  	logging.error("CASE ERROR: COULD NOT PARSE LINE AS A NUMBER!!\n %s"
    	, line)
  	sys.exit(0)


if __name__ == "__main__":
  # OptParse section
  parser = OptionParser()
  parser.add_option("-f", "--file", dest="filename",
    help="load initial topology from FILE", metavar="FILE")
  parser.add_option("-v","--verbose",  action="store_true", dest="verbose",
  	help="Turn on talkative mode")
  
  (options, args) = parser.parse_args()
  

  # filename loading section
  if options.filename:
    filename = options.filename
  else:
    logging.error("Filename not found. Program is exiting")
    sys.exit(0)
  
  # create graph with vertex_number vertex
  # Rationale: do not process variables while read file.
  g = Graph()
  
  # load config-topology from filename with readonly permissions
  f = open(filename, 'r')
  line_numer = 0
  for line in f:
    # first line parsing 
    if line_numer == 0:
      splitted_line = line.split()
      if len(splitted_line) == 2 :
        parse_first_line_config(splitted_line)
      elif len(splitted_line) < 2 :
        sys.exit(0)
      else:
        logging.debug("config file 1st line has to much numbers")
        parse_first_line_config(splitted_line)
    # parsing rest of the config-topology file
    else:
      parse_edges(line)
    line_numer = line_numer+1
  logging.debug("closing file...")
  f.close()
  
  # printing how many vertices are loaded
  target = g.get_vertex(g.get_vertex_number()) # end of the graph
  # Calculating shortest path from 1 to the last vertex
  start_time = datetime.now()
  # Dijkstra algorithm
  dijkstra(g, g.get_vertex(1), target)
  
  path = [target.get_id()]
  shortest(target, path) # sorting 
  print target.get_distance() # OUTPUT
  path = path[::-1] # reverse it
  path_str = ''.join(str(e) + " " for e in path) # making output
  print path_str # OUTPUT
