#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# the directory that contains the test folders
TEST_DIR="testcase_given"

DEBUG_MODE=0

# Check for command line argument to enable debug mode
if [ "$1" == "--debug" ]; then
    DEBUG_MODE=1
fi

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
    echo "Testing $input_file against $output_file"

    # run the python script with the input file and pass the output to diff command and add indentation
    DIFF_OUTPUT=$(diff --strip-trailing-cr <(python3 main.py < $input_file) $output_file)
    DIFF_EXIT_CODE=$?

    if [ $DIFF_EXIT_CODE -ne 0 ]; then
        printf "${RED}Failed${NC}\n"
        if [ $DEBUG_MODE -eq 1 ] && [ ! -z "$DIFF_OUTPUT" ]; then
            echo "---BEGIN DIFF---"
            echo "$DIFF_OUTPUT" | sed 's/^/    /'
            echo "---END DIFF---"
        fi
    else
        printf "${GREEN}Passed${NC}\n"
    fi
  done
done