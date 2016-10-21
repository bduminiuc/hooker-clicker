# coding: utf-8
import argparse
import pyautogui
import csv
from pyhooked import Hook, MouseEvent

def writer():
    def hook_mouse(args):
        if isinstance(args, MouseEvent):
            #print(args)
            pass

    hk = Hook()
    hk.handler = hook_mouse
    hk.hook(mouse=True, keyboard=False)
    

def clicker(logfile):
    with open(logfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            print(" ".join(row))

def argsInit():
    argparser = argparse.ArgumentParser(
        description="")
    group = argparser.add_mutually_exclusive_group()
    group.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Means how many times to repeat")
    group.add_argument(
        "-w", "--write",
        action="store_true",
        help="Add it if you want to write actions")
    return argparser.parse_args()

if __name__ == "__main__":
    logfile = "log.csv"
    args = argsInit()
    if args.write:
        writer(logfile)
    else:
        clicker(logfile)
