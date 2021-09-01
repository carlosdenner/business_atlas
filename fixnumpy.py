import numpy as np
filename = 'tablehdf.h5'

a_file = open(filename)
lines = a_file.readlines()
for line in lines:
  print(line)
a_file.close()