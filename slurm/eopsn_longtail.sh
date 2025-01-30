#!/bin/bash

#SBATCH -N 1                       # Number of nodes
#SBATCH --gres=gpu:1               # Request  GPUs
#SBATCH --partition=gpu_h100      # Partition name (adjust if necessary)
#SBATCH -t 0-20:00                 # Time limit (3 daydef train_tr)
#SBATCH -o "/nfs/homedirs/koerner/Experiments/slurm_eopsn/eopsn_longtail.out"  # Output file path
#SBATCH --mem=64000                # CPU memory 
#SBATCH --qos=deadline              # Quality of service
#SBATCH --cpus-per-task=15          # Number of CPU cores per task

# Set GPU memory constraint if your SLURM setup supports it


cd ${SLURM_SUBMIT_DIR}
echo Starting job ${SLURM_JOBID}
echo SLURM assigned me these nodes:
squeue -j ${SLURM_JOBID} -O nodelist | tail -n +2

# Load and activate the Conda environment
CONDA_BASE=$(conda info --base)
echo $CONDA_BASE
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate eopsn117
cd /nfs/homedirs/koerner/Git/OPS_dual_decision

export DETECTRON2_DATASETS=/nfs/students/koerner/Datasets/
python train_net.py --config-file configs/eopsn_K5.yaml --num-gpus 1 DATALOADER.NUM_WORKERS 10 
