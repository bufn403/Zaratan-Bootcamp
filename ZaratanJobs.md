# Commands to Review Zaratan Compute Resources
1. lscpu 
    - Displays cpu details
2. free -h
    - Displays memory information
3. nvidia-smi
    - checks for Nvidia GPU should be none since they use AMD


# Submitting Jobs
[Documentation](https://hpcc.umd.edu/hpcc/help/jobs.html)

Slurm Job Shell Script: ```process_data_job.sh```

## Job 1: Process the Parquet file into a CSV

Ensure both `process_data.py` and `process_job.sh` are in the same directory. Submit the job script using the `sbatch` command:

```bash
sbatch process_data_job.sh
```

After submission, monitor the job's status with:

```bash
squeue -u $USER
```

## Job 2: Perform Simple Data Analysis on the Advan Data CSV

```bash
sbatch submit_advan_analysis.sh
```

After submission, monitor the job's status with:

```bash
squeue -u $USER
```



Once the job completes, check the output and error files (`ProcessDataJob_<jobID>.out` and `ProcessDataJob_<jobID>.err`) to ensure the script executed successfully and the CSV file was generated.

**Explanation of Slurm Directives:**

- `#!/bin/bash`: Specifies the script should be run in the Bash shell.
- `#SBATCH --job-name=ProcessDataJob`: Names the job "ProcessDataJob".
- `#SBATCH --output=ProcessDataJob_%j.out`: Directs standard output to a file named `ProcessDataJob_<jobID>.out`.
- `#SBATCH --error=ProcessDataJob_%j.err`: Directs standard error to a file named `ProcessDataJob_<jobID>.err`.
- `#SBATCH --time=01:00:00`: Sets a walltime limit of 1 hour.
- `#SBATCH --ntasks=1`: Requests 1 task (core).
- `#SBATCH --mem=8GB`: Allocates 4 GB of memory.

**Explanation of Commands:**
- `module purge`: Clears all loaded modules to ensure a clean environment.
- `module load python/3.10.10`: Loads the Python 3.10.10 module available on Zaratan.
- `python process_data.py`: Executes the Python script.



**Important:**

- **Data Files:** Verify that `advan_jan2020.parquet` is located in the same directory or provide the full path to the file in the Python script.