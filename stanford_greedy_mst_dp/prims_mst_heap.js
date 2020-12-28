const fs = require('fs');
const  Heap = require('../../js-utils/heap');

/** 
Calculates total weight of a MST for the given undirected graph
Uses Prim's algorithm to discover the MST
@param fileName - Path to file representing the graph 
The file shall have n(V) n(E) as the first line, and u v w for each edge in the following lines
V - Set of all vertices
E - Set of all edges
u,v - vertices joined by an edge
w - weight of the above edge
@example - file: 3 2\n1 2 1\n3 2 -2\n represents a graph with 1,2,3 as vertices 
and with 1-2 (1), 1-3 (-2) as edges with edge weights in parenthesis
*/
const findMSTCost = fileName => {
    fs.readFile(fileName,(err,data)=> {
        const edges = data.toString()
        .split('\n')
        .map(strJob => strJob
            .split(' ')
            .map(strVal => Number(strVal)));
    
        const V = edges[0][0];
        const E = edges[0][1]
        
        // trim data
        edges.splice(0,1);
        if (edges.slice(-1)[0] == 0) edges.splice(-1);
        
        // Construct adjacency list representation of the graph
        let G = new Map();
    
        let u,v,e;
        for (let i = 0; i < E; i++) {
            [u,v,e] = edges[i];
            if (G.has(u)) {
                G.set(u,G.get(u).concat([{val:[u,v],priority:e}]));
            }else{
                G.set(u,[{val:[u,v],priority:e}]);
            }
            if (G.has(v)) {
                G.set(v,G.get(v).concat([{val:[u,v],priority:e}]));
            }else{
                G.set(v,[{val:[u,v],priority:e}]);
            }
        }
        const firstNode = G.get(edges[0][0]);
    
        // mark first node as visited
        // add add of its edges to the heap
        let minHeap = new Heap(firstNode).init();
        let visited = new Set([edges[0][0]]);
        
    
        let smallestEdge,u,v,w;
        let mstCost = 0;
        while (minHeap.size && visited.size < V){
    
            // extract the min-weight edge in the cut
            smallestEdge = minHeap.pop()
    
                
            // extract u-v and edge weight
            u = smallestEdge.val[0];
            v = smallestEdge.val[1];
            w = smallestEdge.priority;
    
            let nextVertex;
            if (visited.has(u)){
                if (visited.has(v))
                    continue;
                nextVertex = v;
            }else{
                nextVertex = u;
            }
            minHeap.push(...(G.get(nextVertex)));
            mstCost += w;
            visited.add(nextVertex);
        }
        console.log(mstCost);
    
    });    
}
