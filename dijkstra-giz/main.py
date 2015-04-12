
#!/usr/bin/python
"""
Lukasz Sedek
Polsko-Japonska Akademia Technik Komputerowych
lukasz.sedek(at)pja.edu.pl 
License Apache 2.0
"""
from optparse import OptionParser
import logging, sys
from vertex import Vertex
from graph import Graph


# global variables 
verbose          = True
filename         = ""
vertex_number    = 0
edges_number     = 0

# Parsing 1st line of config-topologu file
# initialize both variables. In case of cast Error, exit
def parse_first_line_config( line ):
  logging.debug("Splitted line: %s", splitted_line)
  try:
    vertex_number = int(line[0])
    logging.info("Vertex number: %s", vertex_number)
    for i in range(0, vertex_number):
    	print "fff"
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
  except ValueError:
  	logging.error("CASE ERROR: COULD NOT PARSE LINE AS A NUMBER!!\n %s"
    	, line)
  	sys.exit(0)


if __name__ == "__main__":
  # OptParse section
  parser = OptionParser()
  parser.add_option("-f", "--file", dest="filename",
    help="load initial topology from FILE", metavar="FILE")
  parser.add_option("-l", "--log", dest="loglevel", default="INFO",
    help="set logging level LOG, DEBUG", metavar="LEVEL")
  (options, args) = parser.parse_args()
  
  # logging utils section
  permitted_log_levels = {"INFO", "DEBUG"}
  if any(options.loglevel.upper() in item for item in permitted_log_levels):
    logging.basicConfig(level=options.loglevel.upper())
  else:
    logging.basicConfig(level="INFO")

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
  print g
  
  # load config-topology from filename with readonly permissions
  f = open(filename, 'r')
  line_numer = 0
  for line in f:
    logging.debug("Line %s : %s", line_numer, line.rstrip('\n'))
    # first line parsing 
    if line_numer == 0:
      logging.debug("First line")
      splitted_line = line.split()
      if len(splitted_line) == 2 :
        logging.debug("config has exact 1st line format")
        parse_first_line_config(splitted_line)
      elif len(splitted_line) < 2 :
        logging.error("MISSING ARGUMENT IN 1ST LINE")
        sys.exit(0)
      else:
        logging.debug("config file 1st line has to much numbers")
        parse_first_line_config(splitted_line)
    else:
      parse_edges(line)
    line_numer = line_numer+1
  logging.debug("closing file...")
  f.close()

