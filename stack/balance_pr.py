#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for i in s:
        if i == "[" or i == "{" or i == "(":
            stack.append(i)
        elif i == "]":
            if stack:
                item = stack.pop(-1)
                if item != "[":
                    return "NO"
            else:
                return "NO"
        elif i == "}":
            if stack:
                item = stack.pop(-1)
                if item != "{":
                    return "NO"
            else:
                return "NO"
        elif i == ")":
            if stack:
                item = stack.pop(-1)
                if item != "(":
                    return "NO"
            else:
                return "NO"
    # print(stack)
    if stack:
        return "NO"
    return "YES"


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    ip = open("ip.txt")
    op = open("op.txt")

    inpts = ip.read().split("\n")[1:]
    ops = op.read().split("\n")
    for i, o in zip(inpts, ops):
        result = isBalanced(i.strip())
        if result != o:
            print(i)
            print(o, result)
            break

    ip.close()
    op.close()
