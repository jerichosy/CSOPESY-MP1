import random

# Y = number of processes (constraints: 3 ≤ Y ≤ 100)
# Z = time slice value (constraints: 1 ≤ Z ≤ 100, applicable to Round-Robin only, if X is not RR then this must be set 1 and ignored)
Y = input("Enter number of processes: ")
# Z = input("Enter time slice value: ")
Z = 3

f_FCFS = open("testcase_FCFS_gen_input.txt", "w")
f_SJF = open("testcase_SJF_gen_input.txt", "w")
f_SRTF = open("testcase_SRTF_gen_input.txt", "w")
f_RR = open("testcase_RR_gen_input.txt", "w")

# Table 1. CPU Scheduling Algorithms and their corresponding value of X.
# | CPU Scheduling Algorithm | Value of X
# |     FCFS	             |     0
# |     SJF	                 |     1
# |     SRTF	             |     2
# |     RR	                 |     3
f_FCFS.write(f"0 {Y} 1\n")
f_SJF.write(f"1 {Y} 1\n")
f_SRTF.write(f"2 {Y} 1\n")
f_RR.write(f"3 {Y} {Z}\n")

# A = process ID
# B = arrival time
# C = burst time
B = random.randint(2, 10)
for A in range(int(Y)):
    B += 1  # + random.randint(2, 10)
    C = random.randint(2, 100)

    f_FCFS.write(f"{A} {B} {C}\n")
    f_SJF.write(f"{A} {B} {C}\n")
    f_SRTF.write(f"{A} {B} {C}\n")
    f_RR.write(f"{A} {B} {C}\n")

f_FCFS.close()
f_SJF.close()
f_SRTF.close()
f_RR.close()
