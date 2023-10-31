// main.js
function algorithmChange() {
    let algorithm = document.getElementById('algorithm').value;
    let timeQuantumDiv = document.getElementById('timeQuantumDiv');

    // If algorithm is RR, show Time Quantum input. Otherwise, hide it.
    if(algorithm === 'RR') {
        timeQuantumDiv.style.display = 'block';
    } else {
        timeQuantumDiv.style.display = 'none';
    }
}

function submitClick() {
    // let strategy = document.getElementById('strategy').value;
    // let arrivalTime = document.getElementById('arrivalTime').value;
    // let burstTime = document.getElementById('burstTime').value;
    // let timeQuantum = document.getElementById('timeQuantum').value;
    // let output = 'Strategy: ' + strategy + '\nArrival Time: ' + arrivalTime + '\nBurst Time: ' + burstTime;

    // // If strategy is RR, add Time Quantum to output.
    // if(strategy === 'RR') {
    //     output += '\nTime Quantum: ' + timeQuantum;
    // }

    // // Output the results in the textbox
    // document.getElementById('output').innerText = output;

    // let encodedStr = encodeURIComponent(document.getElementById('output').value);
    // let dataUri = `data:text/plain;charset=utf-8,${encodedStr}`
    let downloadLink = document.getElementById('download-link');
    // downloadLink.setAttribute('href', dataUri);
    downloadLink.style.display = 'block';
}

function downloadFile() {
    let textFileContent = document.getElementById('output').value;

    let textFileAsBlob = new Blob([textFileContent], {type:'text/plain'});
    let anchor = document.createElement('a');
    anchor.href = URL.createObjectURL(textFileAsBlob);
    anchor.download = 'output.txt';
    anchor.click();
}

document.getElementById('compare').addEventListener('click', function() {
    let output = document.getElementById('output').value;
    let comparisonText = document.getElementById('comparison-box').value;

    if(output === comparisonText) {
        alert('Output MATCHES the comparison text!');
    }
    else {
        alert('Output DOES NOT MATCH the comparison text!')
    }
});
