#!/usr/bin/python3
import sys
def arg():
    args_len = len(sys.argv) -1
    arg_list = sys.argv[1:]
    print(f"{args_len} arguments{':' if args_len > 0 else '.'}")
    for i in range (args_len):
        print (f"{i} :{arg_list[i]}")
    print("\n")
arg()
