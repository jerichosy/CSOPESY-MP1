from typing import List


class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time


def FCFS(processes: List):
    processes.sort(key=lambda Process: Process.arrival_time)

    time_slices = []
    previous_end_time = 0
    for process in processes:
        # start, end, waiting
        time_slices.append(
            (
                process.pid,
                previous_end_time,
                previous_end_time + process.burst_time,
                previous_end_time - process.arrival_time,  # waiting time
            )
        )
        previous_end_time += process.burst_time
    return time_slices


def SJF():
    raise NotImplementedError


def SRTF():
    raise NotImplementedError


def RR():
    raise NotImplementedError


# Table 1. CPU Scheduling Algorithms and their corresponding value of X.
# | CPU Scheduling Algorithm | Value of X
# |     FCFS	             |     0
# |     SJF	                 |     1
# |     SRTF	             |     2
# |     RR	                 |     3


if __name__ == "__main__":
    # X = CPU scheduling algorithm
    # Y = number of processes (constraints: 3 ≤ Y ≤ 100)
    # Z = time slice value (constraints: 1 ≤ Z ≤ 100, applicable to Round-Robin only, if X is not RR then this must be set 1 and ignored)
    X, Y, Z = list(map(int, input().rstrip().split(" ")))
    processes = []
    for _ in range(Y):
        # A = process ID
        # B = arrival time
        # C = burst time
        A, B, C = list(map(int, input().rstrip().split(" ")))
        processes.append(Process(A, B, C))

    if X == 0:
        time_slices = FCFS(processes)
    elif X == 1:
        SJF()
    elif X == 2:
        SRTF()
    elif X == 3:
        RR()

    # print(result)

    avg_waiting_time = 0
    for time_slice in time_slices:
        print(
            f"{time_slice[0]} start time: {time_slice[1]} end time: {time_slice[2]} | Waiting time: {time_slice[3]}"
        )
        avg_waiting_time += time_slice[3]
    avg_waiting_time /= len(time_slices)
    print(f"Average waiting time: {avg_waiting_time}")
