# ND-Crowd-Simulator-Results

This repository contains the results from our sister repository ND-Crowd-Simulator found at https://github.com/emorysmithis/ND-Crowd-Simulator. 

## Files 
- `12_students` through `12000_students` directories contain the output files from our `simulation.py` script found in our sister repository 
- within these directories are subdirectories that separate the simulations of different types 
- The different types of simulations are: 
    - `default` and `default_parallel`: default simulation on the cloud 
    - `local`: default simulation locally 
    - `paths` and `paths_parallel`: n-shortest path simulations in parallel on the cloud 
    - `paths_batch`: n-shortest path simulations in parallel, started in batches, cloud 
    - `speeds_batch`: transportation simulations in parallel, started in batches, cloud 
- see our report and sister repository for more information 
