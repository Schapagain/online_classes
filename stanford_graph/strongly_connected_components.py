


import sys
import threading

class Node:
    def __init__(self,val):
        self.val = val
        self.neighbors = []
        self.leader = None # Used for Kosaraju's algorithm to find SCCs
        self.num_followers = 0 # If the node is a leader, it might have non-zero followers

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


    def add_edge(self,src,dest):
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

        src_node.neighbors.append(dest_node)


    def get_reverse(self):
       g = Graph()
       for vertex in self.vertices:
           if vertex:
               for adjacent in vertex.neighbors:
                   g.add_edge(adjacent.val,vertex.val)
       return g

    def _get_finish_times(self):

        def DFS(source):
            explored.add(source)
            for adjacent in source.neighbors:
                if adjacent not in explored:
                    DFS(adjacent)
            finished.append(source)

        g = self.get_reverse()
        finished = []
        explored = {None}

        for vertex in g.vertices[::-1]:
            if vertex not in explored:
                DFS(vertex)

        return finished

    def get_number_of_SCC(self):

        def DFS(source):
            explored.add(source)
            source.leader = curr_leader
            curr_leader.num_followers += 1
            for adjacent in source.neighbors:
                if adjacent not in explored:
                    DFS(adjacent)

        magic_ordering = self._get_finish_times()[::-1]

        # Get nodes from the original graph using the magic_ordering
        # since get_finish_times returns pointers to nodes in the reverse graph
        magic_ordering = [self.vertices[vertex.val] for vertex in magic_ordering]

        explored = {None}
        num_SCC = 0
        leaders = []

        for vertex in magic_ordering:
            if vertex not in explored:
                curr_leader = vertex
                num_SCC += 1
                leaders.append(curr_leader)
                DFS(vertex)
        return [num_SCC,leaders]

    def print_graph(self):
        for i in range(self.V):
            node = self.vertices[i]
            if node:
                print(node.val,end=': ')
                for adjacent in node.neighbors:
                    print('->',adjacent.val,end='')
                print()
def main():

    try:
        graph_filename = sys.argv[1]
        f = open(graph_filename)
    except:
        exit("Please provide the source of the graph as a command line arguemnt (txt file)")

    G = Graph()
    for edges in f:
        if edges =='':
            break
        src,*vertices = list(map(int,edges.strip().split()))
        for vertex in vertices:
            G.add_edge(src,vertex)

    num_scc,leaders = G.get_number_of_SCC()
    print('number of connected Components',num_scc)

    # sort leaders by follower size
    leaders = sorted(leaders,key = lambda x:x.num_followers,reverse=True)
    for leader in leaders[:5]:
        print(f'leader: {leader.val} followers: {leader.num_followers}')

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=main).start()

