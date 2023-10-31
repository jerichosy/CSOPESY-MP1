// main.js
document.getElementById('submit').addEventListener('click', function() {
    let arrivalTime = document.getElementById('arrivalTime').value;
    let burstTime = document.getElementById('burstTime').value;

    // Print the values in the console
    console.log(`Arrival Time: ${arrivalTime}`);
    console.log(`Burst Time: ${burstTime}`);
});