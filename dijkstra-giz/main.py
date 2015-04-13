
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

# Dijkstra algorithm computing shortest path from start to target
def dijkstra(aGraph, start, target): 
  # Set the distance for the start node to zero 
  start.set_distance(0) # Put tuple pair into the priority queue 
  priority_queue = [(v.get_distance(),v) for v in aGraph] 
  heapq.heapify(priority_queue) 

  while len(priority_queue): 
    # Pops a vertex with the smallest distance 
    uv = heapq.heappop(priority_queue)
    current = uv[1] 
    current.set_visited() 
 
    #for next in v.adjacent: 
    for next in current.adjacent:
      # if visited, skip 
      if next.visited: 
   	    continue
      new_dist = current.get_distance() + current.get_weight(next)

      if new_dist < next.get_distance():
      	next.set_distance(new_dist)
      	next.set_previous(current)
      	logging.debug("updated current: %s, next = %s, new_dist = %s",
      		current.get_id(), next.get_id(), next.get_distance())
      else:
        logging.debug("not updated current: %s, next: %s new_dist = %s ",
         current.get_id(), next.get_id(), next.get_distance())

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

# Parsing 1st line of config-topologu file
# initialize both variables. In case of cast Error, exit
def parse_first_line_config( line ):
  logging.debug("Splitted line: %s", splitted_line)
  try:
    vertex_number = int(line[0])
    logging.info("Vertex number: %s", vertex_number)
    for i in range(1, vertex_number+1):
      g.add_vertex(i)
    edges_number  = int(line[1])
    logging.info("Edge number: %s", edges_number)
  except ValueError:
    logging.error("CASE ERROR: COULD NOT PARSE 1ST LINE AS A NUMBER!!\n %s"
    	, line)
    sys.exit(0)

# Parsing other lines of config-topology file
# initialize 3 tuples. In case of cast Error, exit
def parse_edges(line):
  line_splited = line.split()
  logging.debug("Splitted line %s ", line_splited)
  vertex_1 = 0
  vertex_2 = 0
  weight = 0
  try:
    vertex_1 = int(line_splited[0])
    vertex_2 = int(line_splited[1])
    weight   = int(line_splited[2])
    logging.debug("Adding edge(%s, %s, %s)", vertex_1, vertex_2, weight)
    g.add_edge(vertex_1, vertex_2, weight)
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
  
  # logging utils section
  if options.verbose:
    logging.basicConfig(level="DEBUG", format='%(message)s')

  # filename loading section
  logging.debug("checking filename argument")
  if options.filename:
    logging.debug("options.filename exists: %s", options.filename)
    filename = options.filename
    logging.debug("variable filename sucessfully initialized : %s ", filename)
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
    logging.debug("Line %s : %s", line_numer, line.rstrip('\n'))
    # first line parsing 
    if line_numer == 0:
      splitted_line = line.split()
      if len(splitted_line) == 2 :
        parse_first_line_config(splitted_line)
      elif len(splitted_line) < 2 :
        logging.error("MISSING ARGUMENT IN 1ST LINE")
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
  logging.info("Vertices %s" , g.get_vertices()) 
  target = g.get_vertex(g.get_vertex_number()) # end of the graph
  # Calculating shortest path from 1 to the last vertex
  start_time = datetime.now()
  # Dijkstra algorithm
  dijkstra(g, g.get_vertex(1), target)
  stop_time = datetime.now()
  delta = stop_time - start_time
  logging.debug("Execute time: %s seconds %s microseconds"
  	, delta.seconds, delta.microseconds)
  path = [target.get_id()]
  shortest(target, path) # sorting 
  g.print_graph(path) # making graph.png file
  print target.get_distance() # OUTPUT
  path = path[::-1] # reverse it
  path_str = ''.join(str(e) + " " for e in path) # making output
  print path_str # OUTPUT
