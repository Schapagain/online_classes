const fs = require('fs');
const util = require('util');
const Heap = require('../../js-utils/heap');
const UnionFind = require('../../js-utils/unionFind');;
/** 
*/

class Node {
    constructor(val,weight) {
        this.val = val,
        this.priority = weight,
        this.left = null,
        this.right = null,
        this.rank = 0,
        this.minRank = 0
    }
}

async function encode(fileName) {
    let data;
    try {
        data = await util.promisify(fs.readFile)(fileName);
    } catch (err) { throw err; }

    data = data.toString().split('\n').map(num => Number(num));
    const numSymbols = data[0];
    const heap = new Heap(new Array(numSymbols).fill(0).map((val,i) => new Node(i,data[i+1]))).init(); 

    let newNode;
    while(true) {
        const a = heap.pop();
        const b = heap.pop();

        // merge nodes and push the new one to the heap
        newNode = new Node(Number(a.val.toString().concat(b.val.toString())),a.priority+b.priority);
        
        newNode.rank = Math.max(a.rank,b.rank) + 1;
        newNode.minRank = Math.min(a.minRank,b.minRank) + 1;
        newNode.left = a;
        newNode.right = b;

        if (heap.isEmpty()) break;
        heap.push(newNode);

    }

    return [newNode.minRank,newNode.rank];
}

(async function a(){
    console.time('encoding time');
    const [minLength,maxLength] = await encode('huffman.txt');
    console.timeEnd('encoding time')
    console.log(minLength,maxLength);
})();