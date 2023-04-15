import argparse
from helpers import Solver

parser = argparse.ArgumentParser()

parser.add_argument("--target", type=int)
parser.add_argument("--digits", nargs="+", type=int)

args = parser.parse_args()

print(f'Target: {args.target}')
print(f'Digits: {args.digits}')

solver = Solver(args.target, args.digits)
solver.solve()
