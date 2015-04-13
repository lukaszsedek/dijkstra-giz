import heapq

def dijkstra(aGraph, start, target): 
  print '''Dijkstra's shortest path''' 
  # Set the distance for the start node to zero 
  start.set_distance(0) # Put tuple pair into the priority queue 
  unvisited_queue = [(v.get_distance(),v) for v in aGraph] 
  heapq.heapify(unvisited_queue) 

  while len(unvisited_queue): 
    # Pops a vertex with the smallest distance 
    uv = heapq.heappop(unvisited_queue)
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
      else:
        log.debug("not updated current: %s, next: %s new_dist = %s ",
         current.get_id(), next.get_id(), next.get_distance())

    while len(unvisited_queue):
    	heapq.heappop(unvisited_queue)
    unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
    heapq.heapify(unvisited_queue)

def shortest(v, path):
  ''' make shortest path from v.previous'''
  if v.previous:
    path.append(v.previous.get_id())
    shortest(v.previous, path)
  return