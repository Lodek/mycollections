# Code examples
```python
from import mycollections.graph.graph import Graph

g = Graph()
Node = g.node_factory

n1 = Node(1)
n2 = Node(2, parent=n1)
n3 = Node(3, parents=[n1,n2])
n4 = Node(4, child=n1)

n4.parents.add(n3)

assert n2.parents == [n1]
assert n1.children == [n2,n3]
assert n4.parents == [n3]
```
