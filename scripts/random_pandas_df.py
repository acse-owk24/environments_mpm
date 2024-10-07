import sys 
sys.path.append(".")

from envtest import rand_df

shape = (3,3)

print(rand_df(shape))
