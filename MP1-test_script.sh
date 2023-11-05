#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# the directory that contains the test folders
TEST_DIR="MP1-testcase_given"

echo "Enter the number of the folder to test: "
echo "1) FCFS"
echo "2) RR"
echo "3) SJF"
echo "4) SRTF"
echo "5) ALL"
read -p "Option: " opt

case $opt in
    1) folders=("FCFS") ;;
    2) folders=("RR") ;;
    3) folders=("SJF") ;;
    4) folders=("SRTF") ;;
    5) folders=("FCFS" "RR" "SJF" "SRTF") ;;
    *) echo "Invalid option. Exiting."; exit 1 ;;
esac

for folder in ${folders[@]}; do
  echo ""
  echo "--------------------------------------------------------"
  echo "Testing $folder"
  echo "--------------------------------------------------------"
  for input_file in $(ls $TEST_DIR/$folder/input*.txt); do
    # derive the output file from the input file
    output_file="${input_file/input/output}"
    echo ""
    # echo "--------------------------------------------------------"
    echo "Testing $input_file against $output_file"
    # echo "--------------------------------------------------------"

    # run the python script with the input file and pass the output to diff command
    diff <(python MP1.py < $input_file) $output_file
    if [ $? -ne 0 ]; then
        printf "${RED}Failed${NC}\n"
    else
        printf "${GREEN}Passed${NC}\n"
    fi
  done
done