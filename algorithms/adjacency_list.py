from collections import defaultdict

class AdjList:
  def __init__(self):
    self.nodes = defaultdict(self.Node)

  class Node:
    def __init__(self, node_id=None):
      self.id = node_id
      self.edges = []

    def __lt__(self, other):
      return self.cost < other.cost

  # add_vertex
  def add_node(self, src):
    self.nodes[src].id = src

  def add_edge(self, src, dst, weight):
    self.add_node(src)
    self.nodes[src].edges.append((dst, weight))

  def adjacent(self, n1, n2):
    if len(self.nodes[n1].edges) < len(self.nodes[n2].edges):
      less_edges = n1
      more_edges = n2
    else:
      less_edges = n2
      more_edges = n1

    for i in self.nodes[less_edges].edges:
      if i[0] == more_edges:
        return True
      else:
        return False

  def neighbors(self, node):
    return self.nodes[node].edges

  # complexity: O(V)
  # could split into two methods in order to ease the burden of remove_node
  def remove_edge(self, n1, n2):
    for src, dst in [(n1,n2),(n2,n1)]:
      for i, edge in enumerate(self.nodes[src].edges):
        if edge[0] == dst:
          self.nodes[src].edges.pop(i)
          break
  
  # complexity: O(E)
  def remove_node(self, node):
    for edge in self.nodes[node].edges:
      self.remove_edge(edge[0], node)
    
    del self.nodes[node]

