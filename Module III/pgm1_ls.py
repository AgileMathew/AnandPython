"""Problem 1: Write a program to list all files in the given directory."""

import os
def ls(dirname):
  xs=os.listdir(dirname)
  return xs
print ls("p6")

