# This App Has 2 Functions
# 1st for Finding size of nested folders * it's a tricky job
# 2nd for Deleting nest folders * it's hard too
import os


def get_dir_size(path='.'):
    # size of path in KB
    total = 0

