# This script converts an MP1 test case into a format that can be used by https://boonsuen.com/process-scheduling-solver

import argparse
import os

from utils.utils import Algorithm

# Parsing argument
parser = argparse.ArgumentParser()
parser.add_argument(
    "file_path", type=str, help="The path to the input testcase to be converted."
)
args = parser.parse_args()

# Opening and reading the text file
with open(args.file_path, "r") as file:
    lines = file.readlines()

# Get algorithm and time slice value
X, _, Z = lines[0].rstrip().split(" ")
algorithm = Algorithm(int(X))  # convert X to Algorithm enum

# Get rest of the lines
lines = lines[1:]

# Variables to store the outputs
second_col = []
third_col = []

# Iterating over each line, and appending each columns data
for line in lines:
    row = line.split()
    second_col.append(row[1])
    third_col.append(row[2])

# Writing results to a new file
filename, file_extension = os.path.splitext(os.path.basename(args.file_path))
with open(f"{filename}-boonseun{file_extension}", "w") as out_file:
    out_file.write("For use in https://boonsuen.com/process-scheduling-solver\n\n")
    out_file.write("Converted from " + args.file_path + "\n\n")
    out_file.write("Algorithm: " + algorithm.name + "\n")
    out_file.write("Arrival Times: " + " ".join(second_col) + "\n")
    out_file.write("Burst Times: " + " ".join(third_col) + "\n")

    # If algorithm is Round Robin, then write time slice value
    if algorithm == Algorithm.RR:
        out_file.write("Time Quantum: " + Z + "\n")
