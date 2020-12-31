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
    console.time('knapsack time');
    const solution = await findMaxKnapsackValue('knapsack_big.txt');
    console.timeEnd('knapsack time')
    console.log(solution);
})();