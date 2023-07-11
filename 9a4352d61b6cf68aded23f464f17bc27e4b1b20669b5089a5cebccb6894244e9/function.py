
# > python ./function_block/function.py argv1 argv2 argv3
import sys

# get number of argv
num_args = len(sys.argv)

# no argv
if num_args == 1:
    print("no argv")

# exist argv
else:
    print("number of argv is {}.".format(num_args - 1))
    for i in range(1, num_args):
        print("argv{} is {}.".format(i, sys.argv[i]))
