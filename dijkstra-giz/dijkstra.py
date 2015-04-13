import heapq

'''
Dijkstra algorithm which comuputes shortest path between two vertices.
Used python heapq implementation of priority heap
'''
def dijkstra(graph, start, target): 
  print '''Dijkstra's shortest path''' 
  # 1. Start point is distance 0
  start.set_distance(0) 
  # 2. All other vertices are infinity (done by default on vertex)
  # Put all vertices in priority queue
  priority_queue = [(v.get_distance(),v) for v in graph] 
  heapq.heapify(priority_queue) 

  # 3. While heap is not empty...
  while len(priority_queue): 
    # pop vertex with lowest priority from queue
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
      else:
      	# But if it's not, just skip this point
        log.debug("not updated current: %s, next: %s new_dist = %s ",
        current.get_id(), next.get_id(), next.get_distance())

    # 5. leat but not last pop all from queue
    while len(priority_queue):
    	heapq.heappop(priority_queue)
    priority_queue = [(v.get_distance(),v) for v in graph if not v.visited]
    heapq.heapify(priority_queue)

# sorting vertices of shortest path in python list
def shortest(v, path):
  ''' make shortest path from v.previous'''
  if v.previous:
    path.append(v.previous.get_id())
    shortest(v.previous, path)
  return