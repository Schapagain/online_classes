const fs = require('fs');
const Heap = require('../../js-utils/heap');

fs.readFile('edges.txt',(err,data)=> {
    const edges = data.toString()
    .split('\n')
    .map(strJob => strJob
        .split(' ')
        .map(strVal => Number(strVal)));

    const V = edges[0][0];
    const E = edges[0][1]
    
    // trim data
    edges.splice(0,1);
    edges.splice(-1);
    
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
    
    let cutEdges = [...firstNode];
    let visitedNodes = new Set([edges[0][0]]);

    
    let smallestEdgeIndex;
    let smallestEdge;
    let mstCost = 0;    
    while (visitedNodes.size < V) {
        // pick the min edge in the cut
        smallestEdgeIndex = 0;
        for (let i =0 ; i < cutEdges.length; i++) {
            if (cutEdges[i].priority < cutEdges[smallestEdgeIndex].priority)
                smallestEdgeIndex = i; 
        }
        smallestEdge = cutEdges[smallestEdgeIndex];
        cutEdges.splice(smallestEdgeIndex,1);
        
        // extract u-v and weight of edge
        let u = smallestEdge.val[0];
        let v = smallestEdge.val[1];
        let weight = smallestEdge.priority;

        // check which one is on the outside of the cut
        // if both u and v are contained inside the cut, skip
        let nextVertex;
        if (visitedNodes.has(u)){
            if (visitedNodes.has(v))
                continue;
            nextVertex = v;
        }else{
            nextVertex = u;
        }
        // console.log(nextVertex);
        // push all new edges added to the cut
        cutEdges.push(...(G.get(nextVertex)));
        mstCost += weight;
        visitedNodes.add(nextVertex);
    }
    console.log(mstCost);
});
