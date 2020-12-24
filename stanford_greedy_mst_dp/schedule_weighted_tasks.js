const fs = require('fs');

fs.readFile('jobs.txt',(err,data)=> {
    const jobs = data.toString()
    .split('\n')
    .map(strJob => strJob
        .split(' ')
        .map(strVal => Number(strVal)));

    const numJobs = jobs[0][0];
    const allJobs = jobs.slice(1,numJobs+1);

    // Sort by decreasing order of weight - length
    // Break ties by placing higher weight before lower weight
    allJobs.sort((a,b) => {
        const diff = (b[0] - b[1])-(a[0] - a[1]);
        return diff? diff : b[0] - a[0];
    }); 
    // Sort by decreasing order of w/l
    // allJobs.sort((a,b) => (b[0]/b[1])-(a[0]/a[1]));

    // Find sum of weighted completion times
    let time = 0;
    let weightedSum = 0;
    let currentJob;
    for (let i = 0; i < numJobs; i++) {
        currentJob = allJobs[i];
        weightedSum += currentJob[0] * (currentJob[1]+time);
        time += currentJob[1];
    }
    console.log(weightedSum);
});
