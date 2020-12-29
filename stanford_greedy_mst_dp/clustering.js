const fs = require('fs');
const util = require('util');
const Heap = require('../../js-utils/heap');
const UnionFind = require('../../js-utils/unionFind');;
/** 
Clusters the given points in space using given distance between pairs
Implements max-space k-clustering
returns the separation between two closest points in separate clusters
@param fileName - Path to file representing the graph 
The file shall have n(V) as the first line, and u v d for each pair of points in the following lines
V - Set of all vertices
u,v - points in sample space
d - distance between each pair of points
@example - file: 3\n1 2 1\n3 2 -2\n represents points 1,2,3 in space with d12 = 1, d32 = -2 (all distances are symmetric)
*/
const findMaxSpacing = async (fileName,k) => {
    let data;
    try{
        data = await util.promisify(fs.readFile)(fileName);
    }catch(err){throw err}

    const edges = data.toString()
    .split('\n')
    .map(strJob => strJob
        .split(' ')
        .map(strVal => Number(strVal)));

    const V = edges[0][0];
    
    // trim data
    edges.splice(0,1);
    if (edges.slice(-1)[0] == 0) edges.splice(-1);

    const union = new UnionFind();
    const forest = (new Array(V).fill(0).map((_num,i) => i)).map(name => {
        const tree = union.makeSet();
        tree.name = name;
    
        return tree;
      });

    let heap = new Heap(
        edges.map(edge=>
            ({
                val:edge.slice(0,2),
                priority:edge[2]
            })
            )).init();
    
    let minEdge;
    while (union.numClusters > k) {
        minEdge = heap.pop();

        // extract u-v and edge weight
        u = minEdge.val[0]-1;
        v = minEdge.val[1]-1;
        w = minEdge.priority; 

        // skip if merging would form a cycle
        if (union.find(forest[u]) !== union.find(forest[v])) {
            // else merge clusters containing u and v
            union.union(forest[u],forest[v])
        }
    }

    // find distance between closest, separate points
    let val,priority;
    while(true){
        ({val,priority} = heap.pop());
        if (union.find(forest[val[0]-1]) != union.find(forest[val[1]-1])) return priority;
    }

}

(async function a(){
    console.time('clustering time');
    const maxSpacing = await findMaxSpacing('clustering_small.txt',4)
    console.timeEnd('clustering time')
    console.log(maxSpacing);
})();