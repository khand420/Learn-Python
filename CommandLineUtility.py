import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'sub':
        return args.x - args.y  

    elif args.o == 'mul':
        return args.x * args.y  

    elif args.o == 'div':
        return args.x / args.y   

    else:
        return "Something Went Wrong!"






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number, This is utility for calculation. Please contact Danish Bhai")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number, This is utility for calculation. Please contact Danish Bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is utility for calculation. Please contact Danish Bhai for more")                                        

args = parser.parse_args()
# help to print the value in the console
sys.stdout.write(str(calc(args)))







# # run this command
# # add 
# python CommandLineUtility.py --x 8 --y 9 --o add
# # sub
# python CommandLineUtility.py --x 8 --y 9 --o sub