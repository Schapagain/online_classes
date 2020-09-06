


class Node:
    def __init__(self,val):
        self.val = val
        self.neighbors = []

class Graph:
    def __init__(self,n=0):
        self.V = n
        self.vertices = []
        for i in range(self.V):
            node = Node(i)
            self.vertices.append(node)

    def add_vertex(self,val):
        if self.V <= val:
            self.vertices += [None]*(val-self.V+1)
            self.V = val+1
        node = Node(val)
        self.vertices[val] = node
        return node


    def add_edge(self,src,dest,length):
        try:
            src_node = self.vertices[src]
            if not src_node:
                raise IndexError
        except IndexError:
            src_node = self.add_vertex(src)

        try:
            dest_node = self.vertices[dest]
            if not dest_node:
                raise IndexError
        except IndexError:
            dest_node = self.add_vertex(dest)

        src_node.neighbors.append((dest_node,length))

    def get_V(self):
        return len([vertex for vertex in self.vertices if vertex])

    def print_graph(self):
        for i in range(self.V):
            node = self.vertices[i]
            if node:
                print(node.val,end=': ')
                for adjacent in node.neighbors:
                    print('->',adjacent[0].val,'(',adjacent[1],')',end='')
                print()

    def compute_shortest_paths(self,source):
        source = self.vertices[source]
        explored={source}
        current_cut_edges = [(source,edge) for edge in source.neighbors]
        lengths = [0]*self.V
        paths = [str(source.val)]*self.V
        num_nodes = self.get_V()
        while len(explored)<num_nodes and len(current_cut_edges)>0:
            # minimize lengths[v]+l_vw
            min_cut_edge = min(current_cut_edges,key=lambda x:lengths[x[0].val]+x[1][1])
            current_cut_edges.remove(min_cut_edge)
            source_node = min_cut_edge[0]
            consumed_node = min_cut_edge[1][0]
            if consumed_node not in explored:
                current_length = min_cut_edge[1][1]
                explored.add(consumed_node)
                lengths[consumed_node.val] = lengths[source_node.val] + current_length
                paths[consumed_node.val] = paths[source_node.val] + '->' + str(consumed_node.val)
                current_cut_edges.extend([(consumed_node,edge) for edge in consumed_node.neighbors])
        return lengths+paths

def build_graph(filename):

    f = open(filename)

    G = Graph()
    count = 0
    for edges in f:
        if edges =='':
            break
        count+=1
        src,*vertices = edges.strip().split()
        for dest in vertices:
            vertex,length = list(map(int,dest.split(',')))
            G.add_edge(int(src),vertex,length)
    return G

def main():
    g = build_graph('dijkstraData.txt')
    lengths = g.compute_shortest_paths(1)
    needed_indices = [7,37,59,82,99,115,133,165,188,197]
    for i in needed_indices:
        print(lengths[i],end=',')
    print()

if __name__ == '__main__': main()


