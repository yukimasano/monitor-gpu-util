# monitor-gpu-util
script for monitoring gpu-utilization 

## why
I couldn't figure out a way to monitor the gpu utilization (in terms of %) while having a job running via slurm.
Using this script will create one background process that will monitor this metric and log it to your specified tensorboard directory.

## how to use it
simple:
in your submit script add these lines before:
```
...
TENSORBOARDNAME="experiment1"
DEVICES="1,2"
python monitor.py ${TENSORBOARDNAME} ${DEVICES} & 

python your_main_code.py ${TENSORBOARDNAME} .... 
```
