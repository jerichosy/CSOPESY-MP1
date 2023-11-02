from time import perf_counter

from pyscript import document

from MP1 import Process, format_result, solve
from utils.utils import Algorithm


def simulate(event):
    tic = perf_counter()
    print("Simulate button clicked")

    arrival_time = document.querySelector("#arrivalTime").value
    burst_time = document.querySelector("#burstTime").value
    arrival_time = [int(x) for x in arrival_time.split(" ")]
    burst_time = [int(x) for x in burst_time.split(" ")]
    print(arrival_time)
    print(burst_time)

    if len(arrival_time) != len(burst_time):
        print(
            "Error: Arrival time and burst time must have the same number of processes"
        )
        print(f"Arrival time: {len(arrival_time)}")
        print(f"Burst time: {len(burst_time)}")
        return None
    print("No error")

    processes = []
    process_count = len(arrival_time)
    for i in range(process_count):
        print(i + 1, arrival_time[i], burst_time[i])
        processes.append(Process(i + 1, arrival_time[i], burst_time[i]))
    algorithm = Algorithm[document.querySelector("#algorithm").value].value
    print(algorithm)

    time_quantum = 1
    if algorithm == Algorithm.RR.value:
        time_quantum = int(document.querySelector("#timeQuantum").value)
        print(time_quantum)
        if time_quantum == "":
            print("Error: Time quantum must be set for Round Robin algorithm")
            return None

    time_slices = solve(algorithm, processes, int(time_quantum))
    result = format_result(time_slices, process_count)

    output = document.querySelector("#output")
    output.innerHTML = result

    clk = document.querySelector("#calculationTime")
    toc = perf_counter()
    clk.innerHTML = f"(Took {toc - tic:0.3f} seconds)"

    return None
