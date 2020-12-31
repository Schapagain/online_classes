const fs = require('fs');
const util = require('util');
/** 
*/


async function findMaxIndependentSet(fileName) {
    let data;
    try {
        data = await util.promisify(fs.readFile)(fileName);
    } catch (err) { throw err; }

    data = data.toString().split('\n').map(num => Number(num));
    const V = data[0];
    data.splice(0,1);
    let maxWeights = new Array(V+2);

    maxWeights[0] = maxWeights[1] = 0;
    for (let i = 2; i < V+2; i++) {
        let curr = data[i-2];
        let includeWeight = maxWeights[i-2] + curr;
        let excludeWeight = maxWeights[i-1];
        maxWeights[i] = Math.max(includeWeight,excludeWeight);
    }
    
    // Reconstruction
    let path = new Array(V).fill(0);
    let i = V-1;
    while (i>=0) {
        if (maxWeights[i+1] > maxWeights[i] + data[i]) {
            i--;
        }else{
            path[i] = 1;
            i-=2;
        }
    }

    // Question asked if nodes 1,2,3,4,17,117,517,997 were included in the path
    let nodes = [1,2,3,4,17,117,517,997];
    let solutionString = nodes.map(node => Number(path[node-1])).join('');
    return solutionString;
}

(async function a(){
    console.time('independent set time');
    const solution = await findMaxIndependentSet('test.txt');
    console.timeEnd('independent set time')
    console.log(solution);
})();