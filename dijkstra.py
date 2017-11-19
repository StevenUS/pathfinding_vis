from heapq import heappush, heappop
from adjacency_list import AdjList
from collections import defaultdict

def dijkstra(start, target, graph):
  path = []
  nodes = graph.nodes
  unvisited = [nodes[start]]
  curr = None
  for _, node in nodes.items():
    node.cost = float('inf') if node.id != start else 0
  while curr != nodes[target] and unvisited:
    curr = heappop(unvisited)
    edges = curr.edges
    for dst, wt in edges:
      if nodes[dst].cost > curr.cost + wt:
        nodes[dst].cost = curr.cost + wt
        heappush(unvisited, nodes[dst]) # will get enqued more than once potentially

  if curr == nodes[target]:
    while curr != nodes[start]:
      for dst, _ in curr.edges:
        minimum, _ = curr.edges[0]
        if nodes[dst].cost < nodes[minimum].cost:
          minimum = dst
      path.append(minimum)
      curr = nodes[minimum]

    path = path[::-1]
    path.append(target)

  return path

def main():
  g = AdjList()
  # (src, dest, weight)
  glist = [
    ('a', 'b', 1),
    ('b', 'a', 1),
    ('a', 'c', 3),
    ('c', 'a', 3),
    ('c', 'd', 4),
    ('d', 'c', 4),
    ('d', 'f', 1),
    ('f', 'd', 1),
    ('d', 'g', 2),
    ('g', 'd', 2),
    ('f', 'h', 6),
    ('h', 'f', 6),
    ('h', 'i', 2),
    ('i', 'h', 2),
    ('h', 'j', 2),
    ('j', 'h', 2),
    ('g', 'k', 7),
    ('k', 'g', 7),
    ('j', 'k', 4),
    ('k', 'j', 4),
    ('e', 'k', 1),
    ('k', 'e', 1),
    ('g', 'e', 8),
    ('e', 'g', 8),
    ('e', 'l', 5),
    ('l', 'e', 5),
    ('k', 'l', 3),
    ('l', 'k', 3),
    ('k', 'm', 12),
    ('m', 'k', 12),
    ('g', 'h', 7),
    ('h', 'g', 7)
  ]

  for src, dst, wt in glist:
    g.add_edge(src, dst, wt)
  
  g.add_node('x')
  # print(g.nodes)
  
  # for _, n in g.nodes.items():
  #   print(n.id, n.edges)

  # print(dijkstra('a', 'm', g))
  print(dijkstra('a', 'm', g))

if __name__ == "__main__":
  main()


