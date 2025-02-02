#!/bin/bash
#SBATCH --job-name=advan_analysis
#SBATCH --output=advan_analysis_output.log
#SBATCH --error=advan_analysis_error.log
#SBATCH --time=00:30:00
#SBATCH --mem=8GB
#SBATCH --cpus-per-task=2

module purge
module load python/3.10.10

echo "Starting Python script..."
python simple_advan_analysis.py
echo "Python script completed."