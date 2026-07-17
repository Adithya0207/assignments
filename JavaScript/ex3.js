const marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];

let passedCount = 0;
let failedCount = 0;
let highestMarks = marks[0];
let lowestMarks = marks[0];
let HighestStudent=marks[0];
let lowestStudent=marks[0];

for (let i = 0; i < marks.length; i++) {

    if (marks[i] >= 50) {
        passedCount++;
    } else {
        failedCount++;
    }

    if (marks[i] > highestMarks) {
        highestMarks = marks[i];
        HighestStudent=i;
    }

    if (marks[i] < lowestMarks) {
        lowestMarks = marks[i];
        lowestStudent=i;
    }
}

console.log("Passed Count:", passedCount);
console.log("Failed Count:", failedCount);
console.log("Highest Marks:", highestMarks);
console.log("Top Student :",HighestStudent)
console.log("Lowest Marks:", lowestMarks);
console.log("Low Student :", lowestStudent);