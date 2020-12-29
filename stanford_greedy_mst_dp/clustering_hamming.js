const fs = require('fs');
const util = require('util');
const UnionFind = require('../../js-utils/unionFind');

const findMaxClusters = async (fileName) => {
    let data;
    try{
        data = await util.promisify(fs.readFile)(fileName);
    }catch(err){throw err}

    // split all vertices by newline and
    // remove spacings between bits
    let vertices = data.toString()
    .split('\n')
    .map(strJob => strJob.replace(/ /g,''));

    const V = vertices[0][0];
    
    // trim data
    vertices.splice(0,1);
    if (vertices.slice(-1)[0] == 0) vertices.splice(-1);

    // vertices = ['1001','1100','0101','1001','0010']

    // map bistrings to their indices
    const uniqueVertices = new Map();
    vertices.forEach(name => {
        if (!uniqueVertices.has(name)) uniqueVertices.set(name,uniqueVertices.size);
    });

    const union = new UnionFind();
    const forest = [...uniqueVertices.keys()].map(name => {
        const tree = union.makeSet();
        tree.name = name;
    
        return tree;
      });

    ([...uniqueVertices.keys()]).forEach(vertex => {
        let twoDAway;
        // Generate strings at most two distance away
        for (let i = 0; i < vertex.length; i++) {
            for (let j = i; j < vertex.length; j++) {
                twoDAway = flipBit(vertex,[i,j]);
                
                // check if that exists as a vertex in our graph
                if (uniqueVertices.has(twoDAway)) {
                    let u = uniqueVertices.get(vertex);
                    let v = uniqueVertices.get(twoDAway); 
                    if (union.find(forest[u]) !== union.find(forest[v])){
                        union.union(forest[u],forest[v])
                    }
                }
            }
        }
    })
    return union.numClusters;
}

(async function a(){
    console.time('clustering time');
    const maxSpacing = await findMaxClusters('clustering_big.txt')
    console.timeEnd('clustering time');
    console.log('min clusterings:',maxSpacing);
})();

function flipBit(str,indices) {
    let s = str.split('');

    for (i of indices){
        if (s[i] == '1') s[i] = '0'
        else s[i] = '1'
        if (indices[0] == indices[1]) return s.join('')
    }

    return s.join('')
}