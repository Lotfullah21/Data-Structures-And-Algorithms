import argparse

# create an object of argumentParser library
parser = argparse.ArgumentParser(description="Meow")
# This line adds a command-line argument to the parser. 
parser.add_argument("-n", default=1, help="number of times a cat meow", type=int)
# parse the arguments and store the values in args.
args = parser.parse_args()
# the value stored in n can be accessed through args.n and it is the value the user typed in after space, after -n after space.
for _ in range(args.n):
    print("MEOW")