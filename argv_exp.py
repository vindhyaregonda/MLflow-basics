import sys

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

print(alpha, l1_ratio)

# This code takes two arguments from the command line and prints them. 
# If no arguments are provided, it uses default values of 0.5 for both arguments.