# CSOPESY-MP1
CPU Scheduling Algorithms Simulation:\
FCFS (first-come, first-serve) \SJF (shortest job first) \SRTF (shortest remaining time first) \RR (round-robin)\

# Members
BALCUEVA, Joshua C.\
LA'O, Erin Denise C.\
SY, Matthew Jericho G.

# Requirements:
- Python 3.10 and up (for speedups, use [PyPy](https://www.pypy.org/) instead of [CPython](https://www.python.org/))

# How To Run The Program

1. Launch command prompt (cmd) in the folder containing "main.py"
2. Run code with test_case file using input redirection: \
    a. `python main.py < "testcase.txt"`

3. Optionally, you can run "test_script.sh" using "Git Bash" to test the code using the test cases provided.\
    a. Right click the folder with "test_script.sh", then click the option "Open Git Bash here". \
    b. A Git Bash command prompt should appear, type `./test_script.sh` to run test cases.\
    c. Choose the number of the CPU Scheduling Algorithm you want to test and enter. 
    
    *****
    In the case that the error "python3: command not found" appears. Edit line 46 of "test_script.sh". \
    Edit "python3" -> "python" 

    It should look like this \
    `DIFF_OUTPUT=$(diff --strip-trailing-cr <(python main.py < $input_file) $output_file)`

    Run test_script.sh again, and it should work.
    *****