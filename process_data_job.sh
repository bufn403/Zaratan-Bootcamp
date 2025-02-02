#!/bin/bash
#SBATCH --job-name=ProcessDataJob
#SBATCH --output=ProcessDataJob_%j.out
#SBATCH --error=ProcessDataJob_%j.err
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --mem=8GB

module purge
module load python/3.10.10

echo "Starting Python script..."
python process_data.py
echo "Python script completed."
