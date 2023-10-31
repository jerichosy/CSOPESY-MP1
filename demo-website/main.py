from pyscript import document

# from MP1 import test


def simulate(event):
    print("wow")
    arrival_time = document.querySelector("#arrivalTime").value
    burst_time = document.querySelector("#burstTime").value
    time_quantum = document.querySelector("#timeQuantum").value

    output = document.querySelector("#output")
    output.innerHTML = f"wow\n{arrival_time}\n{burst_time}\n{time_quantum}"

    # print(test())
