#!/bin/bash

#SBATCH -J dhsvm
#SBATCH -N 3
#SBATCH -n 80
#SBATCH -p powerq
#SBATCH -o dhsvm.out
#SBATCH -e dhsvm.err

NUM_RUNS=80
INPUT_FILE="../INPUT.Mercer.3.1.2_Bin"

module load openmpi/gcc/64/1.10.3

mpirun ./DHSVM3.1.2 $INPUT_FILE $NUM_RUNS