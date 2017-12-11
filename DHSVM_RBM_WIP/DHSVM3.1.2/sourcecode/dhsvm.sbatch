#!/bin/bash

#SBATCH -J dhsvm
#SBATCH -N 2
#SBATCH -p quickq
#SBATCH -o dhsvm.out
#SBATCH -e dhsvm.err 

module load openmpi/gcc/64/1.10.3

mpirun -np 2 ./DHSVM3.1.2 ../INPUT.Mercer.3.1.2_Bin $NUM_RUNS