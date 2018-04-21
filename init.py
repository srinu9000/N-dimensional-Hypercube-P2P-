import math

class hypergraph(object):
    def __init__(self, num_dim):

        self.num_dim = num_dim
        self.nodes = []
        self.edges = {}
        self.edgelinks = {}
        self.non_neighbors = {}
        no_of_nodes = int(math.pow(2, num_dim))

        def try_nodes(self):
            for i in range(no_of_nodes):
                self.nodes.append(bin(i)[2:].zfill(num_dim))

        def create_nodes(self):
            for i in range(2 ** self.num_dim):
                node = ''
                for l in range(self.num_dim):
                    x = (i / (2 ** (l))) % 2
                    node = str(x) + node
                self.nodes.append(node)

        create_nodes(self)

        def find_neighbors(self, link):
            neighbors_links = []
            previous_nodes = hypergraph(self.num_dim - 1)
            current_node = previous_nodes.getnodes()
            for i in range(2 ** (self.num_dim - 1)):
                source = list(current_node[i])
                source.insert(self.num_dim - 1 - link, '0')
                neighbors_links.append(self.create_non_neighboredge("".join(source), link))
            return neighbors_links



        def create_edges(self):

            for link in range(self.num_dim):
                neighbors_links = find_neighbors(self, link)
                self.edges.update(dict.fromkeys(neighbors_links, link))
                self.edgelinks.update(
                    dict(zip([(x[0], link) for x in neighbors_links], neighbors_links)))
                self.edgelinks.update(
                    dict(zip([(x[1], link) for x in neighbors_links], neighbors_links)))

        create_edges(self)

        def create_non_neighbors(self):
            nodes = self.nodes
            edges = self.edges.keys()

            for v1 in nodes:
                for v2 in nodes:
                    if v1 < v2 and ((v1, v2) not in edges):
                        self.non_neighbors.update(
                            {(v1, v2): [num_dim - 1 - i for i in range(num_dim) if list(v1)[i] != list(v2)[i]]})

        create_non_neighbors(self)

    def getnodes(self):
        return self.nodes

    def create_non_neighboredge(self, vertex, link):
        targetVertex = list(vertex)
        if vertex[self.num_dim - 1 - link] == '0':
            targetVertex[self.num_dim - 1 - link] = '1'
            edge = (vertex, "".join(targetVertex))
        else:
            targetVertex[self.num_dim - 1 - link] = '0'
            edge = ("".join(targetVertex), vertex)
        return edge