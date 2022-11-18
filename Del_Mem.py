# This App Has 2 Functions
# 1st for Finding size of nested folders * it's a tricky job
# 2nd for Deleting nest folders * it's hard too
import os


def get_dir_size(path='.'):
    # size of path in KB
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size // 1024
            elif entry.is_dir():
                total += get_dir_size(entry.path)

    return total

def deltree(target):
    # delete target directory and its tree
    for d in os.listdir(target):
        os.remove(target + '/' + d)

    os.rmdir(target)
