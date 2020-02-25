from threading import Thread
import time
from tensorboardX import SummaryWriter
import GPUtil
import sys
import random

# Train, etc.


writer = SummaryWriter(f'./runs/{str(sys.argv[1])}')
print(f"using ./runs/{str(sys.argv[1])} to log GPU util",flush=True)
start = time.time()
# give cuda devices as "1,2" or "0" etc.
devices = [int(i) for i in sys.argv[2].split(",")]

while True:
    GPUs = GPUtil.getGPUs()
    for g in devices:
        writer.add_scalar("stats/GPU-util", float(GPUs[g].load), int(time.time()-start))
    time.sleep(50+random.randint(0, 20))
    if time.time()-start > 7200:
        # only monitor first two hours. i.e. around 120 measurements.
        quit()
