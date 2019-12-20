import os
from multiprocessing import Pool

processes = (
    "first_bot.py",
    "second_bot.py",
)


def run_process(process):
    os.system("python2 {}".format(process))


pool = Pool(processes=2)
pool.map(run_process, processes)
