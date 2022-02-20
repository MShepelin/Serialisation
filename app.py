import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('iterations', type=int,
                    help='a number of iterations used to calculate statistics')

args = parser.parse_args()
print(args.iterations)
