const fs = require('fs');
const util = require('util');
/** 
*/


async function findMaxKnapsackValue(fileName) {
    let data;
    try {
        data = await util.promisify(fs.readFile)(fileName);
    } catch (err) { throw err; }

    data = data.toString().split('\n')
    .map(row => row.split(' ').map(num => Number(num)));

    // sort by weights
    const sorted_items = data.slice(1).sort((a,b) => a[1]-b[1])
    const values = sorted_items.map(data => data[0]);
    const weights = sorted_items.map(data => data[1])
    const capacity = data[0][0];
    const numItems = data[0][1];

    let grid = new Array(capacity+1).fill(0).map( () => new Array(numItems+1).fill(0));

    for (let i = 1; i <= capacity; i++) {
        for (let j = 1; j <= numItems; j++) {
            let weight = weights[j-1];
            let value = values[j-1];
            if (i < weight) {
                grid[i][j] = grid[i][j-1];
            }else {
                grid[i][j] = Math.max(grid[i][j-1],grid[i-weight][j-1]+value);
            }
        }
    }
    return grid[capacity][numItems];
}

async function findMaxKnapsackValueCached(fileName) {
    let data;
    try {
        data = await util.promisify(fs.readFile)(fileName);
    } catch (err) { throw err; }

    data = data.toString().split('\n')
    .map(row => row.split(' ').map(num => Number(num)));

    const values = data.slice(1).map(data => data[0]);
    const weights = data.slice(1).map(data => data[1])
    const capacity = data[0][0];
    const numItems = data[0][1];
  
    let cache = new Map();
    function helper(i,currCapacity) {
        if (i <= 0 || currCapacity <= 0) return 0;

        if (cache.has(String(i)+currCapacity)) {
            return cache.get(String(i)+currCapacity)
        }

        let optimal = 0;
        if (currCapacity < weights[i-1] ) {
            optimal = helper(i-1,currCapacity)
        }else{
            optimal = Math.max(helper(i-1,currCapacity),helper(i-1,currCapacity - weights[i-1]) + values[i-1]);
        }

        cache.set(String(i)+currCapacity,optimal);
        return optimal;
    }
    
    let optimalValue = helper(numItems,capacity);
    return optimalValue;
}

(async function a(){
    console.time('cache time');
    const solution2 = await findMaxKnapsackValueCached('knapsack1.txt');
    console.timeEnd('cache time')
    console.time('knapsack time');
    const solution1 = await findMaxKnapsackValue('knapsack1.txt');
    console.timeEnd('knapsack time')
    
    console.log(solution1,solution2);
})();