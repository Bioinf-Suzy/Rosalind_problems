#tree
with open('rosalind_tree.txt') as f:
    list = f.read().splitlines()

n_nodes = int(list[0])
list_of_edges = list[1:]
n_edges = len(list_of_edges)

edges_to_add = (n_nodes - n_edges - 1)

print(edges_to_add)
